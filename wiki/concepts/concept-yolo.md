---
title: YOLO 目标检测框架
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [目标检测, YOLO, one-stage检测, 实时检测]
related:
  - concept-object-detection
  - concept-state-space-models
  - entity-scmamba-yolo
confidence: high
aliases: ["You Only Look Once", "YOLO检测器"]
---

# YOLO 目标检测框架

## 概念定义

**YOLO**（You Only Look Once）是主流的**单阶段（one-stage）目标检测**算法家族，由 Joseph Redmon 等人于 2016 年提出。

## 核心特点

| 特点 | 说明 |
|------|------|
| **单阶段** | 端到端，无需 RPN/ROI Pooling |
| **实时性** | 适合实时检测场景 |
| **网格检测** | 图像划分为网格，直接预测边界框+类别 |
| **版本迭代** | YOLOv1-v11 各版本持续改进 |

## YOLO 家族

| 版本 | 主要改进 |
|------|----------|
| YOLOv1-v3 | 基础架构演进 |
| YOLOv5-v8 | 工程化、精度提升 |
| YOLOv9-v11 | 新技术引入 |
| **Mamba-YOLO** | Mamba 状态空间模型引入 |
| **RT-DETR** | Transformer-based 实时检测 |

## 在主人研究中的位置

主人熟悉：**YOLO、DETR、RT-DETR、Mamba-YOLO**

主人创新：**SCMamba-YOLO** — 在 Mamba-YOLO 基础上改进 EGSSBlock

## 相关概念

- [[concept-object-detection]] — 上位概念
- [[concept-state-space-models]] — SCMamba-YOLO 的技术基础
- [[entity-scmamba-yolo]] — 主人自研的 YOLO 变体

---

*概念页由知识库自动生成*
