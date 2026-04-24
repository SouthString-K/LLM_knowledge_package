---
title: YOLO 目标检测框架
type: concept
created: 2026-04-12
updated: 2026-04-24
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

YOLO（You Only Look Once）是主流的**单阶段（one-stage）目标检测**算法家族，强调端到端预测和实时推理能力。

## 主线特点

| 特点 | 说明 |
|------|------|
| 单阶段 | 不依赖候选框生成阶段，结构更直接 |
| 实时性强 | 常用于机器人、视频理解、工业视觉等场景 |
| 工程演进快 | 各代版本迭代频繁，重视训练技巧与部署效率 |

## 当前知识库中的重要分支

- 标准 YOLO 系列：实时检测主线
- Mamba-YOLO：把状态空间模型引入 YOLO
- SCMamba-YOLO：面向水下海缆检测的任务定制版本

## 新增关联资料

- [[source-2026-04-24-mamba-yolo]] — YOLO 与状态空间模型结合的基础版本
- [[source-2026-04-24-deimv2-dinov3]] — 可作为 YOLO 与 DETR 路线在实时检测上的对照材料

## 相关页面

- [[concept-object-detection]] — 上位概念
- [[concept-state-space-models]] — Mamba / SSM 技术背景
- [[entity-scmamba-yolo]] — 自研 YOLO 变体

---

*概念页由知识库自动生成后持续增量维护*
