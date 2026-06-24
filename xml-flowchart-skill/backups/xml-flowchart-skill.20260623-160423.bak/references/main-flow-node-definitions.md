# Tool 列表

## 1. 2x移动缺陷到屏幕中心 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 2. Area匹配 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ImgMatch |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `TemplateImagePath`: "D:\\RPA\\Share\\Flow\\RPA\\WorkFlows\\127\\f0\\8\\t_8.png"  (类型: System.String)
  - `TemplateRect`: "379.42295895804,488.452129162801,427.797589555903,502.273452190762"  (类型: System.String)
  - `OriginalImagePath`: "D:\\RPA截图\\cell-1_202509151623049233.jpg"  (类型: System.String)
  - `MatchRatio`: 0.88  (类型: System.Double)
  - `EnableLoopMatch`: false  (类型: System.Boolean)
  - `NotFoundExit`: false  (类型: System.Boolean)
  - `MatchInterval`: 0  (类型: System.Int32)
  - `LoopTimeOut`: 0  (类型: System.Int32)
  - `ShowTips`: false  (类型: System.Boolean)
  - `EnableLoopTimeOut`: false  (类型: System.Boolean)
  - `ExitFlowChecked`: false  (类型: System.Boolean)
  - `TimeOutTips`: ""  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "18.裁切后的图像"  (类型: System.String)

---

## 3. End 

| 属性 | 值 |
| :--- | :--- |
| **Type** | RootEnd |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 4. Start 

| 属性 | 值 |
| :--- | :--- |
| **Type** | RootStart |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 5. X 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "绑定变量:43.json取值.值()"  (类型: System.String)
  - `UJsonPath`: "offset_dist[0]"  (类型: System.String)

---

## 6. Y 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "绑定变量:43.json取值.值()"  (类型: System.String)
  - `UJsonPath`: "offset_dist[1]"  (类型: System.String)

---

## 7. act_points 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "103.值"  (类型: System.String)
  - `UJsonPath`: "act_points[0]"  (类型: System.String)

---

## 8. act_re分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 9. act_ta分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 10. action 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "101#s.当前循环值"  (类型: System.String)
  - `UJsonPath`: "action[0]"  (类型: System.String)

---

## 11. change_cam 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "1"  (类型: System.String)

---

## 12. def_name 

| 属性 | 值 |
| :--- | :--- |
| **Type** | StrMatch |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `OCRMode`: 1  (类型: System.Int32)
  - `Languge`: 0  (类型: System.Int32)
  - `CutLeftX`: "$[315.匹配图像的左上角X坐标]"  (类型: System.String)
  - `CutLeftY`: "$[10.匹配图像的左上角Y坐标]"  (类型: System.String)
  - `CutRightX`: "$[315.匹配图像的右下角X坐标]"  (类型: System.String)
  - `CutRightY`: "$[10.匹配图像的右下角Y坐标]"  (类型: System.String)
  - `CroppingRegion`:   (类型: System.String)
  - `OriginalImagePath`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "18.裁切后的图像"  (类型: System.String)

---

## 13. done分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "1000"  (类型: System.String)

---

## 14. go_on 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "1"  (类型: System.String)

---

## 15. go_on流程 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 16. go_on流程分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 17. height 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "103.值"  (类型: System.String)
  - `UJsonPath`: "ta_height"  (类型: System.String)

---

## 18. json取值 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "global.最新的next_request"  (类型: System.String)
  - `UJsonPath`: "request_captures[0]"  (类型: System.String)

---

## 19. loop_find流程分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 20. need_move 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "43.值"  (类型: System.String)
  - `UJsonPath`: "need_move"  (类型: System.String)

---

## 21. re_done分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 22. re_done流程 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 23. recipe 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "103.值"  (类型: System.String)
  - `UJsonPath`: "ta_recipe"  (类型: System.String)

---

## 24. recipe_1 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "158.248679277292,144.396746513965"  (类型: System.String)
  - `MouseEventType`: 4  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "111\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 400  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 25. recipe_2+1 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "1621.01604316537,292.618854578635"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "109\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 26. request_capuures 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "global.最新的next_request"  (类型: System.String)
  - `UJsonPath`: "request_captures[0]"  (类型: System.String)

---

## 27. result_type 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "11.算法结果"  (类型: System.String)
  - `UJsonPath`: "result_type"  (类型: System.String)

---

## 28. to_manual流程分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | VarAssign |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `VarsAssign`: "[{\"TargetUIName\":\"global.单条数据汇总.是否转人工\",\"SourceUIName\":\"1\"}]"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 29. x 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "63.值"  (类型: System.String)
  - `UJsonPath`: "camera_points.offset_dist[0]"  (类型: System.String)

---

## 30. x10 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "1137.62553848941,603.030649476362"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "240\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 1500  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 31. x2 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "1082.23612865025,602.408094402067"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "80\\t_original.png"  (类型: System.String)
  - `PointX`: ""  (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 1500  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 32. y 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "63.值"  (类型: System.String)
  - `UJsonPath`: "camera_points.offset_dist[1]"  (类型: System.String)

---

## 33. 下一个缺陷 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`:   (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 0  (类型: System.Int32)
  - `OriginalImagePath`:   (类型: System.String)
  - `PointX`: "$[18.左上角的X坐标值] + $[10.匹配图像的左上角X坐标]"  (类型: System.String)
  - `PointY`: "$[18.左上角的Y坐标值] + $[10.匹配图像的左上角Y坐标] + 22"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: false  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 34. 保存 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ImgStore |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `StorePath`: "C:\\Users\\PC\\Desktop\\测试"  (类型: System.String)
  - `NameSuffix`: "yyyyMMddHHmmssfff"  (类型: System.String)
  - `SuffixType`: 0  (类型: System.Int32)
  - `IsSharePath`: false  (类型: System.Boolean)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImageName`: ""  (类型: System.String)
  - `UImage`: "18.裁切后的图像"  (类型: System.String)

---

## 35. 修+判分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | BranchStart |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 36. 修补液循环 

| 属性 | 值 |
| :--- | :--- |
| **Type** | LoopStart |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `LoopType`: 0  (类型: System.Int32)
  - `EnableTimeout`: false  (类型: System.Boolean)
  - `TimeoutTips`:   (类型: System.String)
  - `Timeout`: 0  (类型: System.Int32)
  - `TimeoutExitFlow`: false  (类型: System.Boolean)
  - `KeepLoopValue`: false  (类型: System.Boolean)
  - `ShowTips`: false  (类型: System.Boolean)
  - `LimitTimesEnable`: false  (类型: System.Boolean)
  - `LoopMaxTimes`: 0  (类型: System.Int32)
  - `MustRunOnce`: false  (类型: System.Boolean)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `ULoopTimes`:   (类型: System.String)

---

## 37. 偏移记录 

| 属性 | 值 |
| :--- | :--- |
| **Type** | VarAssign |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `VarsAssign`: "[{\"TargetUIName\":\"global.偏移X\",\"SourceUIName\":\"124.值\"},{\"TargetUIName\":\"global.偏移Y\",\"SourceUIName\":\"125.值\"},{\"TargetUIName\":\"global.偏移回offset_x\",\"SourceUIName\":\"124.值\"},{\"TargetUIName\":\"global.偏移回offset_y\",\"SourceUIName\":\"125.值\"}]"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 38. 分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | BranchEnd |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 39. 分支 

| 属性 | 值 |
| :--- | :--- |
| **Type** | BranchStart |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 40. 卸载glass 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ProcessCall |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `FlowId`: "f6"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 41. 变量赋值 

| 属性 | 值 |
| :--- | :--- |
| **Type** | VarAssign |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `VarsAssign`: "[{\"TargetUIName\":\"global.def_name\",\"SourceUIName\":\"30.识别的字符\"},{\"TargetUIName\":\"global.面积\",\"SourceUIName\":\"13.识别的字符\"},{\"TargetUIName\":\"global.glassID\",\"SourceUIName\":\"25.识别的字符\"}]"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 42. 图像匹配 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ImgMatch |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `TemplateImagePath`: "D:\\RPA\\Share\\Flow\\RPA\\WorkFlows\\127\\f0\\278\\t_278.png"  (类型: System.String)
  - `TemplateRect`: "674.377531355489,650.227274488115,722.705120579624,672.514101682075"  (类型: System.String)
  - `OriginalImagePath`: "D:\\RPA\\Data\\Image\\cell_5_202509231444342691.jpg"  (类型: System.String)
  - `MatchRatio`: 0.9  (类型: System.Double)
  - `EnableLoopMatch`: true  (类型: System.Boolean)
  - `NotFoundExit`: true  (类型: System.Boolean)
  - `MatchInterval`: 0  (类型: System.Int32)
  - `LoopTimeOut`: 0  (类型: System.Int32)
  - `ShowTips`: false  (类型: System.Boolean)
  - `EnableLoopTimeOut`: false  (类型: System.Boolean)
  - `ExitFlowChecked`: false  (类型: System.Boolean)
  - `TimeOutTips`: ""  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "177.裁切后的图像"  (类型: System.String)

---

## 43. 字符读取 

| 属性 | 值 |
| :--- | :--- |
| **Type** | StrMatch |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `OCRMode`: 0  (类型: System.Int32)
  - `Languge`: 0  (类型: System.Int32)
  - `CutLeftX`:   (类型: System.String)
  - `CutLeftY`:   (类型: System.String)
  - `CutRightX`:   (类型: System.String)
  - `CutRightY`:   (类型: System.String)
  - `CroppingRegion`: "879.901926472016,676.943470658042,963.784422362231,695.469666069378"  (类型: System.String)
  - `OriginalImagePath`: "25\\t_original.png"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "23.采集的图像"  (类型: System.String)

---

## 44. 巡边流程 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 45. 延迟 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "200"  (类型: System.String)

---

## 46. 当前时间 

| 属性 | 值 |
| :--- | :--- |
| **Type** | CurTime |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `DateFormat`: "yyyyMMdd HHmmss"  (类型: System.String)
  - `EnableOffset`: false  (类型: System.Boolean)
  - `OffsetModel`: 0  (类型: System.Int32)
  - `OffsetValue`: 0  (类型: System.Int32)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 47. 循环 

| 属性 | 值 |
| :--- | :--- |
| **Type** | LoopEnd |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 48. 循环 

| 属性 | 值 |
| :--- | :--- |
| **Type** | LoopStart |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `LoopType`: 0  (类型: System.Int32)
  - `EnableTimeout`: false  (类型: System.Boolean)
  - `TimeoutTips`:   (类型: System.String)
  - `Timeout`: 0  (类型: System.Int32)
  - `TimeoutExitFlow`: false  (类型: System.Boolean)
  - `KeepLoopValue`: false  (类型: System.Boolean)
  - `ShowTips`: false  (类型: System.Boolean)
  - `LimitTimesEnable`: false  (类型: System.Boolean)
  - `LoopMaxTimes`: 3  (类型: System.Int32)
  - `MustRunOnce`: false  (类型: System.Boolean)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `ULoopTimes`:   (类型: System.String)

---

## 49. 报警 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ManualEx |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UMsg`: "未找Area，请人工介入"  (类型: System.String)
  - `UWindowColor`:   (类型: System.String)

---

## 50. 推理服务 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Agent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UAlgoRequestParam`: "global.参数"  (类型: System.String)
  - `UImage`: "34.裁切后的图像"  (类型: System.String)
  - `UPanelImage`: "34.裁切后的图像"  (类型: System.String)
  - `UStepId`: "B19RPAC"  (类型: System.String)
  - `UProductId`: "CELL"  (类型: System.String)
  - `UProductType`:   (类型: System.String)
  - `UTransType`:   (类型: System.String)
  - `USharePath`:   (类型: System.String)
  - `UTimeout`: 10  (类型: System.Int32)
  - `UModelKey`:   (类型: System.String)
  - `UGlassId`: "global.glassID"  (类型: System.String)
  - `UCodeListId`: "1"  (类型: System.String)
  - `ULastCodeListId`: "1"  (类型: System.String)
  - `ULeftCornerPoint`: ""  (类型: System.String)
  - `UDefectId`: "4.时间信息"  (类型: System.String)

---

## 51. 日志 

| 属性 | 值 |
| :--- | :--- |
| **Type** | LogTool |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Name`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UMsg`: "global.左上X"  (类型: System.String)

---

## 52. 流程调用 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ProcessCall |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `FlowId`: "f1"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 53. 涂修补液 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "1423.9666031802,223.031788144371"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "128\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 54. 点击"no" 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "501.988921839901,826.847713594728"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "153\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 55. 点击"yes" 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "409.527471288577,826.324854961671"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "152\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 300  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 56. 点击Area 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "434.359434042965,496.325666057218"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "7\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 100  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 57. 相机倍率 

| 属性 | 值 |
| :--- | :--- |
| **Type** | GetJsonValue |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UJsonObject`: "70.值"  (类型: System.String)
  - `UJsonPath`: "camera_info"  (类型: System.String)

---

## 58. 移动点位 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MovePoints |
| **FlowId** | f3 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UX1`: "global.左上X"  (类型: System.String)
  - `UY1`: "global.左上Y"  (类型: System.String)
  - `UX2`: "global.右下X"  (类型: System.String)
  - `UY2`: "global.右下Y"  (类型: System.String)
  - `UOffsetX`: "global.偏移X"  (类型: System.String)
  - `UOffsetY`: "global.偏移Y"  (类型: System.String)

---

## 59. 第一个缺陷 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ProcessCall |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `FlowId`: "f11"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 60. 等待修补液干 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "60000"  (类型: System.String)

---

## 61. 蓝条匹配 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ImgMatch |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `TemplateImagePath`: "D:\\RPA\\Share\\Flow\\RPA\\WorkFlows\\127\\f0\\10\\t_10.png"  (类型: System.String)
  - `TemplateRect`: "619.429741733195,600.398027282116,644.064703068727,616.031811246779"  (类型: System.String)
  - `OriginalImagePath`: "D:\\RPA\\Data\\Image\\cell_4_202509261008232704.jpg"  (类型: System.String)
  - `MatchRatio`: 0.9  (类型: System.Double)
  - `EnableLoopMatch`: false  (类型: System.Boolean)
  - `NotFoundExit`: false  (类型: System.Boolean)
  - `MatchInterval`: 50  (类型: System.Int32)
  - `LoopTimeOut`: 0  (类型: System.Int32)
  - `ShowTips`: false  (类型: System.Boolean)
  - `EnableLoopTimeOut`: false  (类型: System.Boolean)
  - `ExitFlowChecked`: false  (类型: System.Boolean)
  - `TimeOutTips`: ""  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "18.裁切后的图像"  (类型: System.String)

---

## 62. 裁切 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ImgCropping |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `CutModel`: 1  (类型: System.Int32)
  - `CroppingRegion`:   (类型: System.String)
  - `OriginalImage`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "81.采集的图像"  (类型: System.String)
  - `ULeftX`: "global.左上X"  (类型: System.String)
  - `ULeftY`: "global.左上Y"  (类型: System.String)
  - `URightX`: "global.右下X"  (类型: System.String)
  - `URightY`: "global.右下Y"  (类型: System.String)

---

## 63. 读取Area 

| 属性 | 值 |
| :--- | :--- |
| **Type** | StrMatch |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `OCRMode`: 1  (类型: System.Int32)
  - `Languge`: 0  (类型: System.Int32)
  - `CutLeftX`: "$[8.匹配图像的左上角X坐标]"  (类型: System.String)
  - `CutLeftY`: "$[10.匹配图像的左上角Y坐标]"  (类型: System.String)
  - `CutRightX`: "$[8.匹配图像的右下角X坐标]"  (类型: System.String)
  - `CutRightY`: "$[10.匹配图像的右下角Y坐标]"  (类型: System.String)
  - `CroppingRegion`:   (类型: System.String)
  - `OriginalImagePath`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "18.裁切后的图像"  (类型: System.String)

---

## 64. 调整倍率 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "1081.77756501512,601.603537681038"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "224\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 65. 转人工流程 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`:   (类型: System.String)

---

## 66. 转人工流程 

| 属性 | 值 |
| :--- | :--- |
| **Type** | VarAssign |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `VarsAssign`: "[{\"TargetUIName\":\"global.单条数据汇总.是否转人工\",\"SourceUIName\":\"1\"}]"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 67. 返回原始中心 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ProcessCall |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `FlowId`: "f4"  (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 68. 遍历 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ForeachStart |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UForeachList`: "global.最新的shapes"  (类型: System.String)

---

## 69. 遍历 

| 属性 | 值 |
| :--- | :--- |
| **Type** | LoopEnd |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 70. 遍历研磨点位 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 71. 采集 

| 属性 | 值 |
| :--- | :--- |
| **Type** | CollectionImages |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `IsSimulate`: false  (类型: System.Boolean)
  - `FilePath`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

---

## 72. 键盘 

| 属性 | 值 |
| :--- | :--- |
| **Type** | KeyboardEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Model`: "1"  (类型: System.String)
  - `Keys`:   (类型: System.String)
  - `IndexValue`:   (类型: System.String)
  - `EntryKey`: "BackSpace"  (类型: System.String)
  - `EntryKeyCode`: 8  (类型: System.Int32)
  - `KeyEventType`: 2  (类型: System.Int32)
  - `KeysText`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UInputMsg`: "0.2"  (类型: System.String)

---

## 73. 预留一次涂多个 

| 属性 | 值 |
| :--- | :--- |
| **Type** | Delayed |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UDelayedTime`: "50"  (类型: System.String)

---

## 74. 颜色匹配 

| 属性 | 值 |
| :--- | :--- |
| **Type** | ColorMatch |
| **FlowId** | f9 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `CutLeftX`: "161"  (类型: System.String)
  - `CutLeftY`: "409"  (类型: System.String)
  - `CutRightX`: "162"  (类型: System.String)
  - `CutRightY`: "410"  (类型: System.String)
  - `MinR`: 150  (类型: System.Int32)
  - `MaxR`: 160  (类型: System.Int32)
  - `MinG`: 155  (类型: System.Int32)
  - `MaxG`: 165  (类型: System.Int32)
  - `MinB`: 150  (类型: System.Int32)
  - `MaxB`: 160  (类型: System.Int32)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 0  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**
  - `UImage`: "1.采集的图像"  (类型: System.String)

---

## 75. 鼠标 

| 属性 | 值 |
| :--- | :--- |
| **Type** | MouseEvent |
| **FlowId** | f0 |
| **ParentIdList** | 父节点列表 |
| **ChildrenIdList** | 子节点列表 |
| **IsBreakpoint** | False |

### 参数 (Params)

- **Option**
  - `Points`: "1138.96023959162,601.906888291871"  (类型: System.String)
  - `MouseEventType`: 0  (类型: System.Int32)
  - `ModelType`: 1  (类型: System.Int32)
  - `OriginalImagePath`: "20\\t_original.png"  (类型: System.String)
  - `PointX`:   (类型: System.String)
  - `PointY`:   (类型: System.String)
  - `ExceptionHandlingType`: 0  (类型: BOE.SPCC.Framework.WorkFlow.Tools.BaseV2.ExceptionHandlingType)
  - `RetryCount`: 1  (类型: System.Int32)
  - `RetryInterval`: 1000  (类型: System.Int32)
  - `PostDelay`: 50  (类型: System.Int32)
  - `IsEnable`: true  (类型: System.Boolean)
  - `IsBreakpoint`: false  (类型: System.Boolean)
- **Input**

