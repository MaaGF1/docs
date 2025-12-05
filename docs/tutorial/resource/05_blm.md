# 资源获取：黑铅矿脉（BLM）

本章节详细介绍 MaaGF1 在黑铅矿脉（BLM）中获取资源的策略。

## BLM 概述

黑铅矿脉是一个重要的基础资源点，产出大量的基础材料。

### 地图布局与资源点

![BLM地图](assets/blm_map_overview.png)

*黑铅矿脉的地图概览，标记了主要的资源采集点和敌方巡逻路径。*

## 采集策略

### 推荐队伍与部署

```json
{
  "blm_strategy": {
    "recommended_units": ["Vanguard", "Specialist"],
    "deployment_order": ["A1", "B2", "C3"]
  }
}
```

以上是针对 BLM 效率采集的推荐单位和部署顺序。

### 自动化脚本示例

```python
# BLM 自动化采集脚本片段
def blm_auto_collect():
    print("开始黑铅矿脉自动化采集...")
    # ... 自动化逻辑

blm_auto_collect()
```

## 优化与注意事项

优化路线可以显著提高采集效率。

![优化路线图](img/optimized_path.png)

*经过优化的黑铅矿脉采集路线图，最大化资源获取速度。*
