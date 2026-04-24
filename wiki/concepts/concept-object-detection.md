---
title: 目标检测 (Object Detection)
type: concept
created: 2026-04-12
updated: 2026-04-24
tags: [计算机视觉, 目标检测, 深度学习, YOLO, DETR]
related:
  - concept-yolo
  - concept-state-space-models
  - entity-scmamba-yolo
confidence: high
aliases: ["object detection", "目标检测"]
---

# 目标检测 (Object Detection)

## 概念定义

目标检测是计算机视觉的核心任务之一，旨在**在图像中定位和分类多个目标**。它既回答“图里有什么”，也回答“它在哪里”。

## 主要技术路线

| 路线 | 代表模型 | 特点 |
|------|---------|------|
| Two-stage | Faster R-CNN | 精度高，先提候选区域再分类回归 |
| One-stage | YOLO、SSD | 端到端，推理快，适合实时场景 |
| End-to-end Transformer | DETR、RT-DETR | 去除 NMS / anchor 设计，训练和匹配机制更关键 |

## 主人熟悉的模型

| 模型 | 类型 | 备注 |
|------|------|------|
| YOLO | One-stage | 熟悉主流实时检测路线 |
| DETR / RT-DETR | End-to-end Transformer | 关注匹配策略与实时化 |
| Mamba-YOLO | One-stage + SSM | 用状态空间模型替代部分注意力机制 |
| SCMamba-YOLO | 场景定制模型 | 面向水下海缆检测的改进版本 |

## 新增关联资料

- [[source-2026-04-24-deim]] — 从匹配机制入手提升实时 DETR 的训练效率
- [[source-2026-04-24-deimv2-dinov3]] — 用 DINOv3 特征增强实时检测器
- [[source-2026-04-24-mamba-yolo]] — 用状态空间模型替代自注意力，形成 SSM 检测基线

## 相关概念

- [[concept-yolo]] — 实时 one-stage 检测主线
- [[concept-state-space-models]] — Mamba / SSM 相关建模背景
- [[entity-scmamba-yolo]] — 面向海缆检测的自研变体

---

*概念页由知识库自动生成后持续增量维护*
