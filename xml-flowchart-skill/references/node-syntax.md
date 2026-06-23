# 节点语法参考

本文件用于记录准确的 XML 语法、节点参数、中文/英文别名和连线规则。

检索和归纳节点时，优先使用 `Type` 作为节点类型主键。`Name` 只是显示名或业务名，可能变化；同一个 `Type` 下可能出现多个不同 `Name`，但参数结构通常相同或相近。真实样例可参考 `main-flow-node-definitions.md`。

## 填写方式

每个节点建议使用以下结构：

```markdown
## 节点显示名称

- 标准节点名：
- Type：
- 中文别名：
- 英文别名：
- 业务关键词：
- XML 标签/type：
- 常见 Name：
- 必填参数：
- 可选参数：
- 可选值/枚举：
- 输入端口：
- 输出端口：
- 连线规则：
- 最小 XML 示例：
- 常见错误：
```

## 节点目录

在下方添加节点定义。

<!--
Example:

## 条件判断

- 标准节点名：Decision
- Type：BranchStart
- 中文别名：判断、条件、分支、如果、是否
- 英文别名：condition, branch, if, switch
- 业务关键词：根据条件分流
- XML 标签/type：<node type="decision">
- 常见 Name：分支
- 必填参数：
  - id
  - condition
- 可选参数：
  - description
- 可选值/枚举：
  - operator: equals, contains, greater_than, less_than
- 输入端口：
  - in
- 输出端口：
  - true
  - false
- 连线规则：
  - true 和 false 输出都必须连接到已存在节点。
- 最小 XML 示例：

```xml
<node id="decision_1" type="decision">
  <condition field="status" operator="equals" value="approved" />
  <next port="true" target="approved_end" />
  <next port="false" target="rejected_end" />
</node>
```

- 常见错误：
  - 缺少 false 分支。
-->
