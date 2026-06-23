#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def fail(message):
    print(f"ERROR: {message}")
    return 1


def main():
    if len(sys.argv) != 2:
        return fail("usage: validate_soldata_xml.py <xml-file>")

    path = Path(sys.argv[1])
    raw = path.read_bytes()

    try:
        text = raw.decode("utf-16")
    except UnicodeDecodeError as exc:
        return fail(f"file is not valid UTF-16: {exc}")

    if 'encoding="utf-16"' not in text.splitlines()[0].lower():
        return fail('first line must declare encoding="utf-16"')

    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return fail(f"XML parse failed: {exc}")

    if root.tag != "SolData":
        return fail("root element must be SolData")

    flow_configs = root.find("FlowConfigs")
    if flow_configs is None:
        return fail("missing FlowConfigs")

    if root.find("GlobalQueue") is None:
        return fail("missing root-level GlobalQueue")

    flows = flow_configs.findall("Flow")
    if not flows:
        return fail("FlowConfigs must contain at least one Flow")

    flow_ids = {
        flow.find("Value").attrib.get("Id")
        for flow in flows
        if flow.find("Value") is not None and flow.find("Value").attrib.get("Id")
    }
    errors = []

    for flow in flows:
        key = flow.findtext("Key")
        value = flow.find("Value")
        if value is None:
            errors.append("Flow missing Value")
            continue

        flow_id = value.attrib.get("Id")
        if not key or not flow_id:
            errors.append("Flow must have Key and Value Id")
            continue
        if key != flow_id:
            errors.append(f"Flow Key {key} does not match Value Id {flow_id}")
        runners = value.find("Runners")
        tools = value.find("Tools")
        if runners is None:
            errors.append(f"Flow {flow_id} missing Runners")
        if tools is None:
            errors.append(f"Flow {flow_id} missing Tools")
            continue
        value_children = [child.tag for child in list(value)]
        if "Runners" in value_children and "Tools" in value_children:
            if value_children.index("Runners") > value_children.index("Tools"):
                errors.append(f"Flow {flow_id} must place Runners before Tools")

        tool_map = {}
        for tool in tools.findall("Tool"):
            tool_id = tool.attrib.get("Id")
            tool_type = tool.attrib.get("Type")
            tool_name = tool.attrib.get("Name")
            if not tool_id or not tool_type or tool_name is None:
                errors.append(f"Flow {flow_id} has Tool missing Id/Type/Name")
                continue
            if tool_id in tool_map:
                errors.append(f"Flow {flow_id} duplicate Tool Id {tool_id}")
            tool_map[tool_id] = tool
            if tool.findtext("FlowId") != flow_id:
                errors.append(f"Tool {tool_id} FlowId must be {flow_id}")
            if tool.find("Params") is None:
                errors.append(f"Tool {tool_id} missing Params")
            if tool.find("ParentIdList") is None:
                errors.append(f"Tool {tool_id} missing ParentIdList")
            if tool.find("ChildrenIdList") is None:
                errors.append(f"Tool {tool_id} missing ChildrenIdList")
            if tool.find("IsBreakpoint") is None:
                errors.append(f"Tool {tool_id} missing IsBreakpoint")

        if "t0#s" not in tool_map and flow_id == "f0":
            errors.append("main flow f0 missing RootStart t0#s")
        if "t0#e" not in tool_map and flow_id == "f0":
            errors.append("main flow f0 missing RootEnd t0#e")

        if runners is not None:
            for runner in runners.findall("Runner"):
                source = runner.attrib.get("Id")
                target = runner.attrib.get("Target", "")
                if source not in tool_map:
                    errors.append(f"Runner source {source} not found in Flow {flow_id}")
                for target_id in [part.strip() for part in target.split(",") if part.strip()]:
                    if target_id not in tool_map:
                        errors.append(f"Runner target {target_id} not found in Flow {flow_id}")

        for tool_id, tool in tool_map.items():
            tool_type = tool.attrib.get("Type")
            if tool_type == "RootStart" and not tool_id.endswith("#s"):
                errors.append(f"RootStart Tool {tool_id} should end with #s")
            if tool_type == "RootEnd" and not tool_id.endswith("#e"):
                errors.append(f"RootEnd Tool {tool_id} should end with #e")
            if tool_type in {"BranchStart", "LoopStart", "ForeachStart"} and not tool_id.endswith("#s"):
                errors.append(f"{tool_type} Tool {tool_id} should end with #s")
            if tool_type in {"BranchEnd", "LoopEnd"} and not tool_id.endswith("#e"):
                errors.append(f"{tool_type} Tool {tool_id} should end with #e")
            if tool_type not in {
                "RootStart",
                "RootEnd",
                "BranchStart",
                "BranchEnd",
                "LoopStart",
                "LoopEnd",
                "ForeachStart",
            } and ("#s" in tool_id or "#e" in tool_id):
                errors.append(f"normal Tool {tool_id} of type {tool_type} should not use #s/#e suffix")

            for list_name in ("ParentIdList", "ChildrenIdList"):
                list_node = tool.find(list_name)
                if list_node is None:
                    continue
                for item in list_node.findall("string"):
                    ref = item.text
                    if ref and ref not in tool_map:
                        errors.append(f"Tool {tool_id} {list_name} references missing Tool {ref}")

            parents = [item.text for item in tool.findall("./ParentIdList/string") if item.text]
            children = [item.text for item in tool.findall("./ChildrenIdList/string") if item.text]
            if tool_type != "RootStart" and not parents:
                errors.append(f"Tool {tool_id} ({tool_type}) must have at least one parent")
            if tool_type != "RootEnd" and not children:
                errors.append(f"Tool {tool_id} ({tool_type}) must have at least one child")

            if tool.attrib.get("Type") == "ProcessCall":
                for field in tool.findall("./Params/Param[@Name='Option']/Field[@Name='FlowId']"):
                    target_flow = (field.text or "").strip().strip('"')
                    if target_flow and target_flow not in flow_ids:
                        errors.append(f"ProcessCall Tool {tool_id} references undefined Flow {target_flow}")

            if tool.attrib.get("Type") == "BranchStart":
                children = {
                    item.text for item in tool.findall("./ChildrenIdList/string") if item.text
                }
                for branch in tool.findall("./Condition/Branch"):
                    target = branch.attrib.get("Target")
                    if target and target not in children:
                        errors.append(
                            f"BranchStart Tool {tool_id} branch target {target} not in ChildrenIdList"
                        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: SolData XML structure looks valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
