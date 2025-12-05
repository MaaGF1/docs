# 玩偶行动救援指南

本指南详细介绍了 MaaGF1 在执行玩偶行动时的策略与注意事项。

## 任务概览

玩偶行动是一个资源回收任务，需要精准的部署与时机把握。

### 地图布局

![玩偶行动地图](img/doll_map.png)

*玩偶行动的任务区域地图概览。请仔细研究地图布局与资源点分布。*

## 策略部署

### 阶段一：初期部署

在任务初期，我们需要快速占领关键点。

```python
# 玩偶行动阶段一自动化脚本示例
def deploy_initial_units():
    print("部署初始单位...")
    # ... 更多部署逻辑

deploy_initial_units()
```

### 阶段二：资源回收

回收阶段需要灵活调整队伍，应对突发状况。

![资源回收路线](pic/resource_route.png)

*推荐的资源回收路线，以最大化效率并减少损伤。*

```yaml
# 玩偶行动阶段二配置示例
phase2_config:
  resource_priority: ["iron", "gold"]
  unit_composition: ["defender", "striker"]
```

## 常见问题与优化

如果遇到卡顿或部署失败，请检查您的配置。
