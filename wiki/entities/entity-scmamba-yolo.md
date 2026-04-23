---
title: SCMamba-YOLO
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [目标检测, Mamba, YOLO, 论文创新, ICA-MAl-2026]
related:
  - entity-egssblock
  - concept-state-space-models
  - concept-yolo
  - source-2026-04-12-scamba-yolo
confidence: high
aliases: ["SCMamba-YOLO", "海缆检测YOLO"]
---

# SCMamba-YOLO

## 基本信息

| 项目 | 内容 |
|------|------|
| 全称 | Submarine Cable Mamba-YOLO |
| 类型 | 目标检测模型（基于YOLO + Mamba） |
| 创新来源 | 论文：UW-Cable6K and SCMamba-YOLO (ICA Mal 2026) |
| 状态 | 在投 IEEE ICA Mal 2026 |

## 核心创新

**EGSSBlock**（Edge-Guided State Space Space Block）

- 设计目的：增强边界感知和结构连续性
- 针对任务：水下细长目标（海缆）检测
- 解决的问题：水下图像退化 + 细长目标形态导致的检测困难

## 性能指标

| 指标 | 值 | 说明 |
|------|---|------|
| AP50 | 98.8% | 主流SOTA |
| AP75 | 88.5% | 严格IoU下表现优异 |
| AP50:95 | 78.3% | 全指标优秀 |
| 推理延迟 | 6.0 ms | 轻量实时 |

## 技术架构推测

- **Backbone**：Mamba 状态空间模型（用于长距离依赖建模）
- **Neck**：EGSSBlock（边界引导特征增强）
- **Anchor**：细长目标检测（水下海缆）

## 应用场景

- 海上自动化监控
- 海底基础设施维护
- 实时海缆巡检
- 自动驾驶运输

## 关联论文

- [[source-2026-04-12-scamba-yolo]] — 原始论文

---

*实体页由知识库自动生成*
