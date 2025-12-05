# 资源获取：SKK 后勤部（SKK Logistics）

本章节详细介绍 MaaGF1 在 SKK 后勤部中进行资源管理的策略。

## SKK 后勤部简介

SKK 后勤部是获取经验卡、龙门币等通用资源的主要途径。

### 后勤部地图与效率

![SKK后勤部地图](img/skk_logistics_map.png)

*SKK 后勤部的不同关卡地图，标注了推荐的刷取效率。*

## 收益最大化策略

### 自动刷取配置

```json
{
  "skk_logistics_config": {
    "target_stage": "CE-5",
    "loops": 20,
    "auto_supply": true
  }
}
```

此配置将自动刷取 CE-5 关卡 20 次，并自动补充理智。

### 脚本执行

```bash
# 启动 SKK 后勤部自动化脚本
./maagf1_script run skk_logistics --config default
```

请确保您的脚本是最新版本。

## 效率与时间管理

合理规划每天的理智使用，最大化资源收益。

![理智规划图](assets/sanity_plan.png)

*每日理智使用规划图，助您高效刷取。*
