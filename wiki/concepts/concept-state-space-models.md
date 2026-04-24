---
title: State Space Models (SSM) 状态空间模型
type: concept
created: 2026-04-12
updated: 2026-04-24
tags: [状态空间模型, Mamba, 长距离依赖, 序列建模]
related:
  - concept-yolo
  - entity-scmamba-yolo
  - entity-egssblock
confidence: high
aliases: ["SSM", "State Space Models", "状态空间模型"]
---

# 状态空间模型 (State Space Models, SSM)

## 概念定义

状态空间模型是一类用于建模**长序列依赖关系**的模型路线，源头来自控制理论中的状态空间表示，后来被引入深度学习并形成了 Mamba 等代表性结构。

## 代表结构：Mamba

- 用选择性状态更新机制建模长距离依赖
- 相比标准自注意力，理论复杂度更接近线性
- 在长序列、实时推理和边缘部署场景里很有吸引力

## 在视觉中的价值

| 方向 | 作用 |
|------|------|
| 分类 / 表征学习 | 作为高效视觉骨干 |
| 目标检测 | 替代部分注意力或卷积模块，兼顾速度与全局建模 |
| 场景定制检测 | 便于在特定任务中加入边界感知、结构连续性等先验 |

## 新增关联资料

- [[source-2026-04-24-mamba-yolo]] — SSM 在实时目标检测中的基础路线
- [[source-2026-04-12-scamba-yolo]] — SSM 在水下海缆检测场景下的定制化增强

## 在当前知识库中的位置

- [[concept-yolo]] — 与 YOLO 结合形成实时检测变体
- [[entity-scmamba-yolo]] — 面向海缆检测的具体模型
- [[entity-egssblock]] — 融合边界感知的 SSM 模块

---

*概念页由知识库自动生成后持续增量维护*
