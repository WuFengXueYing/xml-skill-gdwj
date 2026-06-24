#!/usr/bin/env python3
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def fail(message):
    print(f"ERROR: {message}")
    return 1


def load_defined_tool_types():
    skill_root = Path(__file__).resolve().parents[1]
    reference_paths = [
        skill_root / "references" / "main-flow-node-definitions.md",
        skill_root / "references" / "node-syntax.md",
    ]
    defined = set()

    for reference_path in reference_paths:
        if not reference_path.exists():
            continue
        text = reference_path.read_text(encoding="utf-8")
        defined.update(
            item.strip()
            for item in re.findall(r"\|\s*\*\*Type\*\*\s*\|\s*([^|\s]+)\s*\|", text)
        )
        defined.update(
            item.strip()
            for item in re.findall(r"-\s*Type[：:]\s*([A-Za-z0-9_#]+)", text)
        )

    return defined


def main():
    if len(sys.argv) != 2:
        return fail("usage: validate_defined_tool_types.py <xml-file>")

    xml_path = Path(sys.argv[1])
    raw = xml_path.read_bytes()

    try:
        text = raw.decode("utf-16")
    except UnicodeDecodeError as exc:
        return fail(f"file is not valid UTF-16: {exc}")

    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return fail(f"XML parse failed: {exc}")

    defined = load_defined_tool_types()
    if not defined:
        return fail("no defined Tool Type values found in skill reference documents")

    used = sorted({tool.attrib.get("Type", "") for tool in root.findall(".//Tool")})
    missing = [tool_type for tool_type in used if tool_type and tool_type not in defined]

    if missing:
        return fail("undefined Tool Type(s): " + ", ".join(missing))

    print("OK: all Tool Type values are defined in skill reference documents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
