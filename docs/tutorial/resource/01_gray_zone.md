# 资源获取：灰烬之潮（Gray Zone）

本章节介绍 MaaGF1 在灰烬之潮（Gray Zone）中进行资源刷取的攻略。

## 灰烬之潮简介

灰烬之潮是获取特定稀有材料的副本，具有独特的环境机制。

### 地形与敌人分布

![灰烬之潮地图](img/gray_zone_map.png)

*灰烬之潮区域的详细地图，标示了特殊地形和主要敌方单位的分布。*

## 攻略要点

### 核心单位选择

```json
{
  "gray_zone_core_units": [
    {"name": "SilverAsh", "role": "DPS"},
    {"name": "Eyjafjalla", "role": "Caster"}
  ]
}
```

核心单位的选择对通关效率至关重要。

### 自动化流程

```bash
# 自动化灰烬之潮脚本启动命令
maagf1_script run gray_zone --loop 10 --auto-deploy
```

确保脚本配置正确以避免卡顿。

## 资源效率提升

合理的路径规划可以大幅提升资源获取效率。

![高效路线](assets/efficient_path.png)

*针对灰烬之潮的高效资源刷取路线图。*
