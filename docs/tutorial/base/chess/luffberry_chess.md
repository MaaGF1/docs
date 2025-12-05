# 基建系统：鲁弗贝利棋（Luffberry Chess）

本章节详细介绍 MaaGF1 在基建系统中的鲁弗贝利棋玩法与策略。

## 鲁弗贝利棋概述

鲁弗贝利棋是基建系统中一项有趣的策略小游戏，可以获取额外奖励。

### 棋盘布局与规则

![鲁弗贝利棋盘](img/luffberry_chess_board.png)

*鲁弗贝利棋的棋盘布局与基本规则图解。*

## 进阶策略

### 棋子组合推荐

```yaml
# 鲁弗贝利棋推荐棋子组合
chess_pieces:
  - name: "Pawn"
    count: 4
  - name: "Knight"
    count: 2
  - name: "Bishop"
    count: 1
```

不同的棋子组合能带来不同的战术优势。

### 自动化辅助脚本

```python
# 鲁弗贝利棋辅助脚本片段
def solve_luffberry_chess():
    print("正在分析棋局...")
    # ... 棋局分析与行动建议

solve_luffberry_chess()
```

## 奖励与收益

完成鲁弗贝利棋可以获得基建材料和干员信赖奖励。

![奖励列表](assets/rewards_list.png)

*鲁弗贝利棋的奖励列表概览。*
