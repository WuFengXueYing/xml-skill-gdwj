---
name: xml-flowchart-builder
description: 当用户需要把中文业务需求、流程逻辑、工作流说明、节点式流程图设计转换成有效的 XML 流程图/工作流文件时使用本技能。本技能要求 agent 先分析需求，检索节点语法和官方节点说明，绘制并与用户确认 Mermaid 草图，再生成并校验最终 XML。
---
# XML 流程图构建助手

使用本技能，将中文业务需求转换为由预定义节点组成的 XML 流程图或工作流文件。

## 参考资料

只读取当前任务需要的参考文件：

- `references/node-syntax.md`：节点名称、中文别名、XML 定义、参数、必填字段、可选值、连线语法和示例。
- `references/main-flow-node-definitions.md`：从真实主流程整理出的节点定义参考，包含大量 Tool 的 `Type`、参数字段和示例值。
- `references/official-node-behavior.md`：每个工具的具体作用说明，包含工具业务作用、适用场景、专属输入输出和限制；不包含通用公共参数。
- `references/examples.md`：真实或已确认的“需求 -> Mermaid 草图 -> XML”案例【目前为空，不支持查看】。
- `references/typical-error-cases.md`：典型错误案例库，记录生成 XML 或流程设计中出现过的问题、关键词、原因和修复方式。
- `references/typical-success-cases.md`：典型成功案例库，记录验证成功的需求、Mermaid 草图、XML 设计要点、关键词和可复用模式。

优先使用关键词检索，而不是一次性读取整份大文档。检索词应包含：节点 `Type`、节点中文名、英文名、别名、参数名、业务功能词、用户原话中的关键词。

节点检索时优先按 `Type` 区分节点类型。节点 `Name` 可能只是业务显示名，例如多个不同 Name 都可能是同一个 `Type=Delayed` 或 `Type=GetJsonValue`；真正决定 XML 参数结构的是 `Type`。

选择节点时先用 `official-node-behavior.md` 判断工具是否适合当前业务动作，再用 `node-syntax.md` 和 `main-flow-node-definitions.md` 查该 `Type` 的完整 XML 参数名、公共参数、ValueType 和示例写法。

注意：`official-node-behavior.md` 不列出公共参数，例如 `ExceptionHandlingType`、`RetryCount`、`RetryInterval`、`PostDelay`、`IsEnable`、`IsBreakpoint` 等。生成 XML 时不能因为作用说明文档没有这些字段就省略它们；完整参数结构以 `node-syntax.md` 和真实节点样例为准。

## 硬性要求

必须先设计 Mermaid 草图, 根据用户的反馈后才设计xml

## 工作流程

1. 解析调研报告或用户材料。

   - 默认用户提供的是调研报告、操作手法总结、现场 SOP、案例表格或半结构化说明，而不是已经整理好的流程图。
   - 先提取报告中的场景、缺陷类型、输入信号、判断依据、人工操作步骤、修复/处理手法、例外情况、失败条件、终止条件。
   - 从多个操作示例中归纳共同流程，不要只复刻单个案例。
   - 将报告内容整理成“场景 -> 判断条件 -> 推荐动作 -> 后续检查 -> 异常/转人工”的结构。
   - 区分事实和推断：报告中明确写出的规则作为事实；为了覆盖更多情况而补充的流程分支必须标记为推断或待确认。
   - 对中文业务词进行归一化，例如“判断/分流/如果”可能对应条件节点，“循环查找/重复确认”可能对应循环节点，“流程调用/返回原点/复检”可能对应子流程或流程调用节点。
   - 如果报告存在互相矛盾、缺少阈值、缺少动作参数、无法判断优先级等问题，先列出待确认点。
2. 构想覆盖性自动流程。

   - 基于调研报告设计一个尽可能覆盖所有情况的自动操作流程，而不是只满足一条用户口头需求。
   - 优先覆盖高频场景、风险场景、明确规则场景；低置信度场景应设计转人工、报警或保守退出路径。
   - 把复杂任务拆成主流程和可复用子流程，例如采集/定位、算法判断、手法选择、执行修复、复检、返回原点、异常处理。
   - 为每个关键判断补充分支：成功、失败、未识别、低置信度、超阈值、无需处理、无法自动处理。
   - 如果需要覆盖“尽可能多情况”，Mermaid 草图中应体现兜底分支，不能只画理想路径。
3. 检索参考资料。

   - 在 `node-syntax.md` 中查询节点定义、XML 语法、参数、必填项和连线规则。
   - 在 `official-node-behavior.md` 中按工具中文名、功能词、输入输出查询候选节点的官方作用、限制和推荐用法；该文档不包含通用公共参数。
   - 在 `main-flow-node-definitions.md` 中优先按 `Type` 查询同类节点样例，再参考 `Name`、业务关键词和参数名，确定 XML 字段写法。
   - 如果存在案例，在 `examples.md` 中检索相似业务场景。
   - 不要凭空编造节点名、参数名、枚举值或 XML 标签；这些内容必须来自参考资料或用户明确提供的信息。
   - 如果用户说的是业务动作，例如“延迟/等待/分支占位”，应先映射到候选 `Type`，再查该 Type 的参数模板。
4. 必须先设计 Mermaid 草图。

   - 绘制 Mermaid 流程图，展示节点顺序、分支条件、循环、异常路径和结束状态。
   - 节点标签优先使用中文业务名称，并在必要时附上参考资料中的节点标准名。
   - 对从调研报告推断出来的分支，在节点或说明中标注“推断/待确认”。
   - 草图应先表达业务逻辑完整性，再映射到具体 XML 节点。
   - 将 Mermaid 草图展示给用户，请用户确认或修改。
   - 这一阶段只交付 Mermaid 草图、流程说明、覆盖范围和待确认点；不要生成 XML。
5. 与用户迭代确认。

   - 根据用户反馈修改 Mermaid 草图，直到用户确认流程正确。
   - 用户新增或修改需求时，先同步更新草图，再生成 XML。
   - 如果现有节点无法表达某个行为，说明最接近的可支持方案，并等待用户确认。
   - 用户确认时，应同时确认：场景是否覆盖充分、分支优先级是否正确、哪些情况转人工、哪些参数/阈值仍待补充。
   - 必须获得用户明确确认，例如“确认”“可以”“按这个生成 XML”“草图没问题”等，再进入 XML 生成阶段。
   - 如果用户只是继续补充需求、提出问题或讨论方案，继续修改 Mermaid 草图，不要提前生成 XML。
6. 生成 XML。

   - 只基于用户已明确确认的 Mermaid 草图和参考资料中的语法生成 XML。
   - 如果没有已确认 Mermaid 草图，必须先回到草图阶段，不能直接生成 XML。
   - 先套用“XML 关键语法”中的固定骨架，再填充流程、连线和节点。
   - 先根据流程图生成节点顺序和连线，也就是 `Runners`；再生成每个 `Tool` 的参数、条件、父子列表。
   - 补齐所有必填参数。
   - 保持分支标签、执行顺序、节点 ID、连线关系一致。
   - 除非目标系统要求特定 ID 格式，否则使用可读、稳定、可复现的 ID。
7. 交付前校验。

   - 确认每个节点类型都能在参考资料中找到。
   - 确认所有必填参数都已填写。
   - 确认所有连线都指向已存在节点。
   - 确认每个分支条件都有目标节点。
   - 确认 XML 格式良好。
   - 确认输出文件按 UTF-16 保存，并且 XML 声明为 `encoding="utf-16"`。
   - 必须运行本技能自带 XML 校验器：`python3 scripts/validate_soldata_xml.py <xml-file>`。
   - 如果校验器不可用，必须明确告诉用户“未完成校验”，不能声称 XML 已可用。
8. 交付后收集反馈。

   - 生成并校验 XML 后，主动请用户反馈：
     - 这个 XML 是否有用，是否能导入或运行。
     - 哪些地方需要改进，例如流程逻辑、节点选择、参数、连线、编码、校验、草图确认流程。
   - 如果用户反馈失败或需要修改，先判断是否属于典型错误；必要时检索 `typical-error-cases.md` 和 `typical-success-cases.md`。
   - 如果形成了可复用经验，先告诉用户自己总结了哪些经验、准备写入哪个文档、计划追加哪些要点；必须等用户明确同意后，才可以修改案例库。

## 调研报告解析规则

当输入是 Excel、Word、PDF、Markdown、截图文字或长篇调研报告时，先完成业务归纳，再进入 Mermaid 和 XML：

- 抽取报告中的术语表：缺陷名称、手法名称、检测结果、设备动作、坐标/倍率/灰阶/尺寸等关键变量。
- 抽取条件表：例如“缺陷超过阈值但不导致 NG”“未找到缺陷点”“同坐标有/无线缺”“无法修补”“需要暗点化”等。
- 抽取动作表：例如采集、定位、移动、切换相机/倍率、zapping、cut、暗点化、补液、复检、报警、转人工。
- 抽取例外表：无法定位、算法低置信度、重复缺陷、超出可修范围、修复后仍 NG、报告中规则冲突。
- 如果报告包含截图或示例图片，必须把图片作为一等输入解析：观察界面区域、缺陷位置、编号、弹窗、按钮、参数区、列表记录、测量线/框/坐标等视觉证据。
- 对图文混合 Excel，不能只读单元格文本；应检查工作簿中的嵌入图片、图片锚点位置、图片顺序和附近文字。必要时把图片导出或渲染成总览图逐张查看。
- 为每张关键图片建立“图像证据卡”：图片/锚点位置、展示场景、可见输入、人工操作、判断结果、后续动作、无法辨认的信息。
- 归纳主流程：采集输入 -> 识别/定位 -> 分类判断 -> 选择手法 -> 执行动作 -> 复检 -> 成功结束或异常处理。
- 归纳子流程：把可复用动作拆为子流程，例如“返回原始中心”“缺陷定位”“执行某类手法”“复检判断”。
- 形成覆盖矩阵：每类场景至少对应一个处理路径；没有自动路径的场景必须有转人工/报警/保守退出路径。
- 不要把报告中的每一行机械翻译成一个节点；应先抽象成规则、决策表和可复用流程。
- 当图片承担主要信息时，Mermaid 草图前先输出一个简短的“报告理解摘要”，说明从图片中识别出的操作模式和不确定点。
- 如果截图中文字过小、分辨率不足或关键弹窗看不清，应明确标为“图片信息不足/待确认”，不要臆造参数。
- 如果报告是 `.xls` 等旧格式且无法完整读取，应告知用户并尽量使用可抽取文本；必要时请用户另存为 `.xlsx`、`.csv` 或导出 PDF。

## Mermaid 草图确认门禁

本技能的核心交互顺序是：调研报告/需求解析 -> Mermaid 草图 -> 用户讨论修改 -> 用户确认最终草图 -> XML 生成 -> XML 校验。

必须遵守：

- 不要在第一次分析需求后直接输出 XML。
- 不要跳过 Mermaid 草图，即使流程看起来简单。
- 不要把 Mermaid 草图和最终 XML 混在同一次交付中，除非用户已经在前文明确确认草图。
- 草图阶段应主动邀请用户修改，例如确认分支、循环、子流程、兜底转人工、参数阈值。
- 用户未确认草图时，最终回复应停留在草图和问题清单，不应继续生成 XML。
- 用户确认草图后，再进入 XML 阶段，并说明 XML 是基于哪个已确认版本生成的。
- 如果用户明确说“跳过草图，直接生成 XML”，仍应先给出一个极简 Mermaid 或文字流程摘要供用户确认；除非用户再次明确要求直接输出 XML，才可跳过。

## 反馈与案例沉淀

当用户对生成结果给出反馈时，按以下方式处理：

- 正向反馈：如果 XML 成功导入/运行，询问是否将该需求、关键词、Mermaid 草图、关键 XML 设计和成功原因沉淀到 `references/typical-success-cases.md`。
- 负向反馈：如果 XML 失败、导入报错、流程不符合预期或参数错误，询问是否将错误现象、关键词、失败原因、修复方法沉淀到 `references/typical-error-cases.md`。
- 写入案例库前，必须先向用户说明：
  - 总结出的经验是什么。
  - 准备写入 `typical-success-cases.md` 还是 `typical-error-cases.md`。
  - 将追加哪些关键词和案例要点。
  - 等用户明确同意后再执行写入。
- 案例必须包含关键词，便于后续快速检索。
- 案例应保留高价值信息：用户需求摘要、相关 Type、相关节点名、错误/成功原因、修复/复用方式、校验结果。
- 不要把一次性的长 XML 全量粘进案例库；只保留必要片段和定位信息。
- 用户未同意前，不要修改任何案例库文件。

## Skill 自检进化

当用户要求“自检 skill”“根据案例优化 skill”“迭代 skill”“复盘错误/成功案例并修改 skill”时，必须执行以下流程：

1. 先检索并阅读 `references/typical-error-cases.md` 和 `references/typical-success-cases.md` 中相关案例。
2. 归纳拟修改内容，明确说明：
   - 发现了哪些重复错误或成功模式。
   - 准备修改哪些文件，例如 `SKILL.md`、`node-syntax.md`、案例库或校验脚本。
   - 修改的主要内容和预期收益。
3. 在修改前必须复制当前版本作为备份。备份建议放在 `backups/` 目录，文件名包含日期时间，例如 `backups/SKILL.md.20260623-153000.bak`。
4. 在真正修改前，必须先把“拟修改内容”和“备份路径”告诉用户，并等待用户明确同意。
5. 用户同意后才可以修改 skill 文件或 reference 文件。
6. 修改完成后，说明实际修改内容，并提示用户可以用一个历史需求重新验证。

禁止事项：

- 不要在用户未同意前修改 skill 本体、reference 或脚本。
- 不要在未备份前修改。
- 不要因为单个失败案例就大幅重写 skill；优先沉淀案例，再抽象稳定规则。
- 不要删除旧规则，除非用户明确确认或新案例证明旧规则有害。

## XML 关键语法

以下规则来自真实样例 `main_flow.xml` 和 `tool_example.xml`。生成 XML 时必须遵守这些结构，避免语法错误。

### 固定文件骨架

XML 文件开头固定为：

```xml
<?xml version="1.0" encoding="utf-16"?>
<SolData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <FlowConfigs>
    ...
  </FlowConfigs>
  <GlobalQueue />
</SolData>
```

要求：

- 根节点必须是 `SolData`，并带有 `xmlns:xsd` 和 `xmlns:xsi` 两个命名空间属性。
- `FlowConfigs` 是流程配置容器，所有流程都放在里面。
- 根级 `GlobalQueue` 放在 `FlowConfigs` 之后；无队列时写成 `<GlobalQueue />`。
- 文件声明写 `encoding="utf-16"`；实际保存也应使用 UTF-16 编码。

### Flow 流程定义

每个流程使用一个 `<Flow>` 表示，结构如下：

```xml
<Flow>
  <Key>f0</Key>
  <Value Id="f0" Name="主流程">
    <Runners>
      ...
    </Runners>
    <Tools>
      ...
    </Tools>
    <GlobalVars />
  </Value>
</Flow>
```

要求：

- `Key` 必须等于 `Value` 的 `Id`。
- 主流程固定使用 `f0`，名称通常为 `主流程`。
- 如果需要子流程，应在 `FlowConfigs` 下新增同级的独立 `<Flow>`，不是嵌套在主流程内部。例如主流程后再写一个 `Key=f1`、`Value Id="f1"`、`Name="子流程1"` 的 `<Flow>`。
- `ProcessCall` 节点若引用 `"f1"`、`"f3"` 等流程 ID，对应 ID 必须在 `FlowConfigs` 中有实际 `<Flow>` 定义；只引用不定义会导致流程不完整。
- 每个 `Value` 内部顺序通常为 `Runners`、`Tools`、可选的 `SubFlows`、可选的 `GlobalVars`。
- 主流程样例中 `Tools` 后有 `<SubFlows />` 和 `<GlobalVars />`；即使子流程以同级 `<Flow>` 存放，主流程仍可保留空的 `<SubFlows />`。
- 无全局变量时写 `<GlobalVars />`。
- Tool ID 的作用域是单个 Flow。不同流程内可以重复使用 `t0#s`、`t0#e`、`1` 等 ID；但同一个 Flow 内不能重复。

### Tool ID 命名规则

根据样例，ID 后缀和节点类型存在稳定约定：

- 流程开始/结束节点使用 `t0#s` 和 `t0#e`。
- 成对控制节点使用同一个数字编号加后缀：
  - 分支：`15#s` 是 `BranchStart`，`15#e` 是 `BranchEnd`。
  - 循环：`44#s` 是 `LoopStart`，`44#e` 是 `LoopEnd`。
  - 遍历：`101#s` 是 `ForeachStart`，对应结束节点通常是 `101#e` 且 Type 为 `LoopEnd`。
- 普通业务节点不需要 `#s/#e`，通常直接使用数字 ID，例如 `1`、`2`、`22`。
- 不要给普通业务节点随意添加 `#s/#e`；不要给 `BranchStart`、`LoopStart`、`ForeachStart` 省略 `#s`；不要给对应结束节点省略 `#e`。
- 同一对控制节点必须使用相同基础编号，例如 `27#s` 对应 `27#e`。
- `Runners`、`ParentIdList`、`ChildrenIdList`、`Condition Branch Target` 中引用节点时，必须使用完整 ID，包括 `#s` 或 `#e` 后缀。

### Runners 连线表

`Runners` 描述节点之间的执行连线：

```xml
<Runners>
  <Runner Id="t0#s" Target="1" />
  <Runner Id="1" Target="t0#e" />
</Runners>
```

要求：

- XML 中应先定义节点顺序，再定义节点参数：在每个 `Value` 内，`Runners` 必须出现在 `Tools` 前面。
- 生成时先从 Mermaid/流程图得到完整边列表，再写 `<Runner>`；不要先写 Tool 参数再临时拼连线。
- 每条连线使用 `<Runner Id="当前节点ID" Target="目标节点ID" />`。
- `Id` 必须是当前流程 `Tools` 中存在的 Tool ID。
- `Target` 可以是单个目标，也可以用英文逗号连接多个目标，例如 `Target="13,28"`。
- `Target` 中的每个目标 ID 都必须在当前流程 `Tools` 中存在。
- `Runners`、`ParentIdList`、`ChildrenIdList` 三处连线必须互相一致。
- 如果节点只有一个出边，写一条 `Runner`；如果节点有多条出边，`Target` 使用英文逗号合并多个目标。
- 如果节点没有出边，例如 `RootEnd`，不要为它写 `Runner`。

示例流程图：

```text
t0#s -> 1 -> 5#s -> 2 -> 7#s -> 8 -> 7#e -> 5#e -> 3 -> 6#s -> 4 -> 6#e -> t0#e
```

对应 `Runners`：

```xml
<Runner Id="t0#s" Target="1" />
<Runner Id="1" Target="5#s" />
<Runner Id="5#s" Target="2" />
<Runner Id="2" Target="7#s" />
<Runner Id="7#s" Target="8" />
<Runner Id="8" Target="7#e" />
<Runner Id="7#e" Target="5#e" />
<Runner Id="5#e" Target="3" />
<Runner Id="3" Target="6#s" />
<Runner Id="6#s" Target="4" />
<Runner Id="4" Target="6#e" />
<Runner Id="6#e" Target="t0#e" />
```

### Tool 节点通用结构

每个节点使用 `<Tool>` 表示：

```xml
<Tool Id="1" Type="CollectionImages" Name="采集">
  <FlowId>f0</FlowId>
  <Params>
    <Param Name="Option">
      ...
    </Param>
    <Param Name="Input" />
  </Params>
  <ParentIdList>
    <string>t0#s</string>
  </ParentIdList>
  <ChildrenIdList>
    <string>t0#e</string>
  </ChildrenIdList>
  <IsBreakpoint>false</IsBreakpoint>
</Tool>
```

要求：

- `Tool` 必须有 `Id`、`Type`、`Name` 三个属性。
- `FlowId` 必须等于当前所在流程的 `Value Id`。
- `Params` 下通常包含 `Param Name="Option"` 和 `Param Name="Input"`。
- 没有输入参数时，`Input` 可写成 `<Param Name="Input" />`。
- `ParentIdList` 放所有父节点 ID；无父节点时写 `<ParentIdList />`。
- `ChildrenIdList` 放所有子节点 ID；无子节点时写 `<ChildrenIdList />`。
- `ParentIdList` 是父节点 ID 列表；`ChildrenIdList` 是子节点 ID 列表，可能包含多个子节点，例如分支开始节点。
- 空父子列表只能用于真实没有父/子节点的起止场景：`RootStart` 可以没有父节点，`RootEnd` 可以没有子节点。
- 普通业务节点、分支/循环/遍历开始节点和结束节点一般都必须同时有父节点和子节点；如果 `ParentIdList` 或 `ChildrenIdList` 为空，通常就是语法/结构错误。
- `IsBreakpoint` 通常写 `false`，并与 Option 中的 `IsBreakpoint` 保持一致。
- 大样例中普通节点还常见 `<SpotId>cell_5</SpotId>`；如果目标系统要求保留布局/位置标识，可照样例加入。

### Option 通用字段

大多数节点的 `Param Name="Option"` 都包含以下通用字段：

```xml
<Field Name="ExceptionHandlingType" ValueType="BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType">0</Field>
<Field Name="RetryCount" ValueType="System.Int32">1</Field>
<Field Name="RetryInterval" ValueType="System.Int32">1000</Field>
<Field Name="PostDelay" ValueType="System.Int32">0</Field>
<Field Name="IsEnable" ValueType="System.Boolean">true</Field>
<Field Name="IsBreakpoint" ValueType="System.Boolean">false</Field>
```

要求：

- 不确定节点特殊配置时，保留这些通用字段。
- `System.Boolean` 值使用小写 `true`/`false`。
- 字符串参数通常使用 `ValueType="System.String"`；样例中部分字符串值带外层英文双引号，例如 `"1"`、`"f1"`、`"global.变量名"`，应参考具体节点样例。
- 空字段可写成自闭合形式：`<Field Name="DirPath" ValueType="System.String" />`。

### RootStart 与 RootEnd

每个流程应包含开始和结束节点。起止节点也必须带完整的 `Params`，不要写成 `<Params />`。标准模板如下：

```xml
<Tool Id="t0#s" Type="RootStart" Name="Start">
  <FlowId>f0</FlowId>
  <Params>
    <Param Name="Option">
      <Field Name="ExceptionHandlingType" ValueType="BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType">0</Field>
      <Field Name="RetryCount" ValueType="System.Int32">1</Field>
      <Field Name="RetryInterval" ValueType="System.Int32">1000</Field>
      <Field Name="PostDelay" ValueType="System.Int32">0</Field>
      <Field Name="IsEnable" ValueType="System.Boolean">true</Field>
      <Field Name="IsBreakpoint" ValueType="System.Boolean">false</Field>
    </Param>
    <Param Name="Input" />
  </Params>
  <Condition />
  <ParentIdList />
  <ChildrenIdList>
    <string>1</string>
  </ChildrenIdList>
  <IsBreakpoint>false</IsBreakpoint>
</Tool>
<Tool Id="t0#e" Type="RootEnd" Name="End">
  <FlowId>f0</FlowId>
  <Params>
    <Param Name="Option">
      <Field Name="ExceptionHandlingType" ValueType="BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType">0</Field>
      <Field Name="RetryCount" ValueType="System.Int32">1</Field>
      <Field Name="RetryInterval" ValueType="System.Int32">1000</Field>
      <Field Name="PostDelay" ValueType="System.Int32">0</Field>
      <Field Name="IsEnable" ValueType="System.Boolean">true</Field>
      <Field Name="IsBreakpoint" ValueType="System.Boolean">false</Field>
    </Param>
    <Param Name="Input" />
  </Params>
  <Condition />
  <ParentIdList>
    <string>3</string>
  </ParentIdList>
  <ChildrenIdList />
  <IsBreakpoint>false</IsBreakpoint>
</Tool>
```

要求：

- 主流程开始节点 ID 使用 `t0#s`，结束节点 ID 使用 `t0#e`。
- 子流程也使用 `t0#s` 和 `t0#e` 作为该子流程自己的开始/结束节点。
- `RootStart` 和 `RootEnd` 的 `Params` 必须包含 `Param Name="Option"` 的通用字段，以及空的 `<Param Name="Input" />`；不要把起止节点写成 `<Params />`。
- `RootStart` 通常无父节点，`ChildrenIdList` 指向第一个业务节点。
- `RootEnd` 通常无子节点，`ParentIdList` 来自最后一个业务节点。
- `RootStart` 和 `RootEnd` 都保留空 `<Condition />`，以贴近系统导出模板。

### 分支节点

分支使用成对节点：

```xml
<Tool Id="15#s" Type="BranchStart" Name="分支">
  ...
  <Condition>
    <Branch Expression="$[8.是否匹配成功]" Target="13" />
    <Branch Expression="!$[8.是否匹配成功]" Target="28" />
  </Condition>
  ...
</Tool>

<Tool Id="15#e" Type="BranchEnd" Name="分支">...</Tool>
```

要求：

- 分支开始节点 ID 使用 `数字#s`，类型为 `BranchStart`。
- 分支结束节点 ID 使用相同数字加 `#e`，类型为 `BranchEnd`。
- `BranchStart` 的 `ChildrenIdList` 应列出所有分支首节点。
- `Condition` 下每个 `<Branch>` 的 `Target` 必须出现在 `ChildrenIdList` 中。
- 分支可以只有一个无表达式入口，例如 `<Branch Target="2" />`；这表示从分支开始进入该子路径。
- 表达式中的 XML 特殊字符必须转义，例如双引号写 `&quot;`，与号写 `&amp;`。
- 多个分支最终通常汇入对应的 `BranchEnd`。
- `BranchEnd` 的父节点通常是各分支路径末端，子节点是分支汇合后的下一个节点。

### 循环与遍历

普通循环使用：

```xml
<Tool Id="44#s" Type="LoopStart" Name="循环">...</Tool>
<Tool Id="44#e" Type="LoopEnd" Name="循环">...</Tool>
```

遍历使用：

```xml
<Tool Id="101#s" Type="ForeachStart" Name="遍历">...</Tool>
<Tool Id="101#e" Type="LoopEnd" Name="遍历">...</Tool>
```

要求：

- `LoopStart`/`ForeachStart` 使用 `#s`，对应结束节点通常使用 `LoopEnd` 和同号 `#e`。
- `LoopStart` 的 Option 常见循环字段包括 `LoopType`、`EnableTimeout`、`Timeout`、`LimitTimesEnable`、`LoopMaxTimes`、`MustRunOnce` 等。
- `ForeachStart` 的输入常见字段为 `UForeachList`，例如 `"global.最新的shapes"`。
- `ForeachStart` 的 `Condition` 可使用无表达式分支指向遍历体首节点，例如 `<Branch Target="8" />`。
- 遍历结束节点使用 `Type="LoopEnd"`，Name 可为 `遍历`，例如 `7#e`。
- 普通循环即使只执行一个内部节点，也应按 `LoopStart -> 内部节点 -> LoopEnd` 结构表达。
- 循环流程默认由 `LoopStart` / `LoopEnd` 控制节点自身处理是否继续循环；不要为了表达无限循环而在 `Runners` 中手动写 `LoopEnd -> LoopStart` 回边。真实导出常见写法是 `LoopEnd -> RootEnd` 或后续节点，但运行时循环语义由循环节点配置决定。
- 当用户描述“无限循环、无退出条件、持续运行直到手动终止”时，应设置 `LoopType`、`MustRunOnce`、`EnableTimeout=false`、`LimitTimesEnable=false` 等循环参数，而不是额外添加普通执行连线回到循环开始节点。
- 循环/遍历内部节点必须能通过 `Runners` 到达对应结束节点或后续节点，不能悬空；同时保持 `Runners`、`ParentIdList`、`ChildrenIdList` 一致。

### 流程图到 XML 的映射

当用户提供实际流程图截图时，按图形语义还原 XML：

- 圆形/起止点：映射为 `RootStart` / `RootEnd`，主流程 ID 通常为 `t0#s` / `t0#e`。
- 矩形业务步骤：映射为普通业务 Tool，例如采集、清晰度检测、数据、流程调用、推理服务。
- 菱形或控制节点：通常映射为 `BranchStart`、`ForeachStart`、`LoopStart` 等开始控制节点。
- 椭圆形带 `#e` 的节点：通常是对应控制结构的结束节点，例如 `BranchEnd` 或 `LoopEnd`。
- 图中箭头顺序优先用于生成 `Runners`；节点框文字用于确定 Tool 的 `Id`、`Name`、`Type` 和后续参数。
- 对照 XML 时，图中 `5#s.分支`、`5#e.分支` 必须成为同一组分支；`7#s.遍历`、`7#e.遍历` 必须成为同一组遍历；`6#s.循环`、`6#e.循环` 必须成为同一组循环。
- 先保证图上的箭头完整表达为 `Runners`，再检查每个 Tool 的 `ParentIdList` 和 `ChildrenIdList` 是否与箭头一致。对循环控制节点要尊重真实导出语义：不要把 Mermaid 中的循环回路机械翻译成 `LoopEnd -> LoopStart` 普通回边。

### 流程调用

子流程调用使用 `ProcessCall`：

```xml
<Tool Id="22" Type="ProcessCall" Name="流程调用">
  <FlowId>f0</FlowId>
  <Params>
    <Param Name="Option">
      <Field Name="FlowId" ValueType="System.String">"f1"</Field>
      ...
    </Param>
    <Param Name="Input" />
  </Params>
  ...
</Tool>
```

要求：

- Tool 内部的 `<FlowId>` 表示当前节点属于哪个流程。
- Option 里的 `<Field Name="FlowId">"f1"</Field>` 表示要调用的目标流程。
- 目标流程 ID 必须在 `FlowConfigs` 中以同级 `<Flow>` 定义，例如：

```xml
<Flow>
  <Key>f1</Key>
  <Value Id="f1" Name="子流程1">
    <Runners>...</Runners>
    <Tools>...</Tools>
  </Value>
</Flow>
```

- 子流程内部 Tool 的 `<FlowId>` 必须写子流程自己的 ID，例如 `f1`。
- 子流程内部的 `Runners`、`ParentIdList`、`ChildrenIdList` 只引用本子流程内的 Tool ID，不直接引用主流程节点。

### 生成前结构清单

生成 XML 前先构造一张节点表，至少包含：

- `id`：节点 ID，例如 `1`、`15#s`、`15#e`、`t0#s`。
- `type`：节点类型，例如 `RootStart`、`CollectionImages`、`BranchStart`。
- `name`：中文显示名。
- `flowId`：所属流程 ID。
- `parents`：父节点 ID 列表。
- `children`：子节点 ID 列表。
- `params`：Option/Input 参数。
- `condition`：分支或循环条件。

然后由这张表生成 `Runners`、`Tools`、`ParentIdList`、`ChildrenIdList`，不要手工分别编三套连线。

生成顺序建议：

1. 从 Mermaid/流程图抽取节点表和边列表。
2. 根据边列表写 `Runners`。
3. 根据节点表写 `Tools`。
4. 对每个 Tool，从边列表反推 `ParentIdList` 和 `ChildrenIdList`。
5. 最后填入 `Params`、`Condition`、`IsBreakpoint` 等参数内容。
6. 保存为 UTF-16 后，必须运行 `scripts/validate_soldata_xml.py` 校验；校验失败不得交付为最终 XML。

## 输出格式

除非用户另有要求，最终回复应包含：

1. 已确认流程的简短说明。
2. 使用 `xml` 代码块输出最终 XML。
3. 必要的假设、待确认点或无法支持的细节。

如果在工作区创建文件，使用清晰的中文或拼音文件名保存 XML，并告知用户绝对路径。

## 编写规则

- 除非用户明确要求直接生成 XML，否则不要跳过 Mermaid 草图确认。
- 不要依赖记忆生成节点语法，必须检索参考资料。
- 官方节点作用说明不要堆进 `SKILL.md`，应放在 references 中。
- XML 尽量简洁；除非目标系统支持注释，否则不要加入 XML 注释。
- 参考资料冲突时，语法以 `node-syntax.md` 为准，节点含义以 `official-node-behavior.md` 为准。
- 面向中文用户沟通时，解释、问题和总结使用中文；XML 标签和参数名按官方语法保持原样。
