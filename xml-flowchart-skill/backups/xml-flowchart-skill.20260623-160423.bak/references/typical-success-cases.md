# 典型成功案例库

用于记录已经验证成功的需求、Mermaid 草图设计、XML 设计要点和可复用模式。后续遇到相似需求时，先按关键词检索本文件。

## 案例模板

```markdown
## 成功案例：简短标题

- 关键词：
- 需求摘要：
- 相关节点 Type：
- 相关节点 Name：
- Mermaid 草图要点：
- XML 设计要点：
- 成功原因：
- 校验方式：
- 可复用模式：
```

## 案例

在下方追加案例。


## 成功案例：图像匹配成功点击失败跳过并循环

- 关键词：无限循环, 图像匹配, 鼠标点击, 失败跳过, 0ms 延迟, LoopStart, LoopEnd
- 需求摘要：循环采集屏幕图像，模板匹配成功则按匹配框坐标偏移点击，匹配失败则跳过点击，延迟后继续循环。
- 相关节点 Type：CollectionImages, ImgMatch, BranchStart, BranchEnd, MouseEvent, Delayed, LoopStart, LoopEnd
- 相关节点 Name：采集, 图像匹配, 分支, 鼠标, 跳过点击, 延迟, 循环
- Mermaid 草图要点：Start -> LoopStart -> 采集 -> 图像匹配 -> 分支；成功路径到鼠标，失败路径到“跳过点击”占位；两路汇入 BranchEnd -> 延迟 -> LoopEnd -> End。
- XML 设计要点：循环不写 `LoopEnd -> LoopStart` 普通回边，循环语义由 `LoopStart/LoopEnd` 参数控制；失败分支使用 `Delayed(0ms)` 占位节点再汇入 `BranchEnd`；三套连线结构保持一致。
- 成功原因：避免手动回连破坏循环控制节点语义，同时避免空分支直接跳控制结束节点，并保证 `Runners`、`ParentIdList`、`ChildrenIdList` 同源一致。
- 校验方式：`scripts/validate_soldata_xml.py` 通过；额外检查 Runner/父子列表一致；用户反馈修正后可正常执行。
- 可复用模式：对“匹配成功执行动作、失败跳过、循环重试”的流程，使用“失败占位节点 + 控制节点原生循环语义”的结构。
