# 典型错误案例库

用于记录 XML 流程图生成中的典型失败、错误模式和修复方法。后续遇到相似需求时，先按关键词检索本文件。

## 案例模板

```markdown
## 错误案例：简短标题

- 关键词：
- 相关需求：
- 相关节点 Type：
- 相关节点 Name：
- 错误现象：
- 根因分析：
- 修复方式：
- 校验方式：
- 可复用规则：
```

## 案例

在下方追加案例。


## 错误案例：Runner 与父子列表不一致导致执行异常

- 关键词：Runner, ParentIdList, ChildrenIdList, 连线不一致, XML 能解析但执行失败
- 相关需求：生成带循环、分支、延迟的 RPA XML 流程。
- 相关节点 Type：RootStart, RootEnd, LoopStart, LoopEnd, BranchStart, BranchEnd
- 相关节点 Name：Start, End, 循环, 分支
- 错误现象：XML 标签可解析，基础校验可能通过，但运行时节点调度异常、分支或循环走向不符合预期。
- 根因分析：`Runners` 中的 Target 与对应 Tool 的 `ChildrenIdList` 不一致，或某节点的 `ParentIdList` 与实际入边不一致；执行器可能读取其中一套结构，导致流程图语义分裂。
- 修复方式：从同一张边表统一生成 `Runners`、`ParentIdList`、`ChildrenIdList`；修改任意连线时必须同步更新三处。对 `LoopEnd -> RootEnd` 这类结构出口，也要保证 RootEnd 的父节点和 LoopEnd 的子节点同步。
- 校验方式：除运行 `scripts/validate_soldata_xml.py` 外，再做一次入边/出边一致性检查：每个节点的 `ChildrenIdList` 必须等于 `Runners` 的 Target，每个节点的 `ParentIdList` 必须等于所有指向它的 Runner 来源。
- 可复用规则：不要分别手工维护三套连线；所有连线都从节点表/边表反推生成。

## 错误案例：失败分支直接跳 BranchEnd 不稳定

- 关键词：BranchStart, BranchEnd, 失败分支, 直接汇合, 空路径, 跳过点击, 0ms 延迟
- 相关需求：图像匹配成功时点击，匹配失败时跳过点击并继续后续延迟/循环。
- 相关节点 Type：BranchStart, BranchEnd, Delayed, MouseEvent, ImgMatch
- 相关节点 Name：分支, 跳过点击, 鼠标, 图像匹配
- 错误现象：匹配失败路径直接从 `BranchStart` 指向 `BranchEnd` 时，部分执行器导入或执行不稳定，可能不触发汇合后的节点。
- 根因分析：控制节点到控制结束节点的空分支路径缺少实际业务节点，某些运行时要求每个分支 Target 指向普通节点或真实分支路径首节点。
- 修复方式：为“无需动作/跳过操作”的分支增加一个普通占位节点，例如 `Delayed` 节点，`UDelayedTime="0"`，命名为“跳过点击”，再从该节点连到 `BranchEnd`。
- 校验方式：检查 `BranchStart` 的每个 `Branch Target` 都在 `ChildrenIdList` 中，并且每条分支路径最终汇入同一 `BranchEnd`；运行 XML 校验和实际导入验证。
- 可复用规则：当某个分支语义是“什么也不做”时，不要直接 Target 到 `BranchEnd`，优先用 0ms `Delayed` 或本系统认可的空操作节点占位。
