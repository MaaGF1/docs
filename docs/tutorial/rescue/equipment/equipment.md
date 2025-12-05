# 装备救援行动

本文档旨在指导用户在 MaaGF1 中进行装备救援行动的规划与执行。

## 任务介绍

装备救援行动是获取稀有装备的重要途径，但挑战性较高。

### 装备掉落概览

![装备掉落概率](assets/equipment_drop_rates.png)

*此图表展示了不同任务中稀有装备的掉落概率，请作为参考。*

## 策略分析

### 推荐队伍配置

```json
{
  "team_config": {
    "main_damage": "Sniper",
    "support": "Medic",
    "tank": "Defender"
  }
}
```

此配置旨在提供均衡的输出与生存能力。

### 行动路线规划

![推荐路线](img/recommended_route.jpg)

*针对装备救援行动的推荐行进路线，标注了潜在的危险区域。*

```bash
# 示例命令：启动装备救援脚本
./maagf1_cli start-mission --type equipment-rescue --config default
```

## 进阶技巧

熟练掌握撤退与再部署的时机是成功的关键。
