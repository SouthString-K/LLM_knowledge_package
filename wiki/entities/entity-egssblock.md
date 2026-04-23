---
title: EGSSBlock
type: entity
created: 2026-04-12
updated: 2026-04-12
tags: [模型架构, 状态空间模型, 边界感知, 论文创新]
related:
  - entity-scmamba-yolo
  - concept-state-space-models
confidence: high
aliases: ["Edge-Guided State Space Block", "边界引导状态空间块"]
---

# EGSSBlock

## 基本信息

| 项目 | 内容 |
|------|------|
| 全称 | Edge-Guided State Space Block |
| 类型 | 模型架构模块 |
| 来源 | SCMamba-YOLO 论文创新（ICA Mal 2026） |
| 发明者 | 主人（论文一作） |

## 设计目的

专门为**水下细长目标检测**设计，解决：
1. **水下图像退化** — 模糊、噪声、低对比度
2. **细长目标形态** — 海缆形状细长，边界不清晰

## 核心功能

- **边界感知（Edge Perception）** — 增强海缆边界特征响应
- **结构连续性（Structural Continuity）** — 保持细长目标完整性

## 在 SCMamba-YOLO 中的位置

推测为 Neck 或 Backbone 中的关键模块，与 Mamba 状态空间模型结合使用。

## 关联实体

- [[entity-scmamba-yolo]] — EGSSBlock 的宿主模型
- [[concept-state-space-models]] — 技术基础

---

*实体页由知识库自动生成*
