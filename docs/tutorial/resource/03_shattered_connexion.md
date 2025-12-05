# 资源获取：破碎连接（Shattered Connexion）

本章节指导用户如何在 MaaGF1 中有效刷取破碎连接活动资源。

## 破碎连接活动概述

破碎连接是限时活动，提供特殊的活动代币和稀有材料。

### 活动关卡布局

![破碎连接关卡图](assets/sc_map_layout.png)

*破碎连接活动关卡的完整布局，包含所有部署点和敌方路径。*

## 刷取策略

### 效率优化队伍

```yaml
# 破碎连接效率刷取队伍配置
team_comp:
  leader: "Blaze"
  vanguard: "Bagpipe"
  medic: "Nightingale"
  snipers: ["Archetto", "Exusiai"]
```

此配置旨在最大化清理速度。

### 脚本自动化

```python
# 破碎连接活动脚本示例
def farm_shattered_connexion():
    print("开始刷取破碎连接...")
    # ... 自动化逻辑

farm_shattered_connexion()
```

## 注意事项

活动期间需关注最新的关卡特性。

![活动机制](img/event_mechanics.png)

*破碎连接活动中的特殊机制说明图。*
