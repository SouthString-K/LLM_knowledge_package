---
title: 目标检测 (Object Detection)
type: concept
created: 2026-04-12
updated: 2026-04-12
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

目标检测是计算机视觉的核心任务之一，旨在**在图像中定位和分类多个目标**。既需要定位（where）又需要识别（what）。

## 两大范式

| 范式 | 代表模型 | 特点 |
|------|---------|------|
| **两阶段（Two-stage）** | Faster R-CNN | 高精度，RPN + ROI |
| **单阶段（One-stage）** | YOLO、SSD | 实时性好，端到端 |

## 主人熟悉的模型

| 模型 | 类型 | 备注 |
|------|------|------|
| **YOLO** | One-stage | 实时检测，熟悉全系列 |
| **DETR** | Two-stage + Transformer | Transformer-based 检测 |
| **RT-DETR** | One-stage + Transformer | 实时 DETR |
| **Mamba-YOLO** | One-stage + SSM | 状态空间模型 + YOLO |

## 主人创新

**SCMamba-YOLO**：在 Mamba-YOLO 基础上改进 EGSSBlock，用于水下海缆检测，性能达 98.8% AP50

## 核心指标

| 指标 | 说明 |
|------|------|
| AP50 | IoU=0.5 下的平均精度 |
| AP75 | IoU=0.75 下的平均精度（更严格）|
| AP50:95 | IoU 从 0.5 到 0.95 的平均精度 |

## 相关概念

- [[concept-yolo]] — 熟悉的检测框架
- [[concept-state-space-models]] — 新一代建模技术
- [[entity-scmamba-yolo]] — 主人自研检测器

---

*概念页由知识库自动生成*
