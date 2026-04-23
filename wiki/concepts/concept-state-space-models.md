---
title: State Space Models (SSM) 状态空间模型
type: concept
created: 2026-04-12
updated: 2026-04-12
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

状态空间模型是一类用于建模**序列数据长距离依赖**的深度学习模型。最早源于控制理论中的状态空间表示，后被引入深度学习。

## 代表模型：Mamba

**Mamba**（2023/2024）是目前最主流的 SSM 架构：
- 提出选择性状态空间机制（Selective State Space Mechanism）
- 可以像 Transformer 一样建模长依赖，同时计算高效（线性复杂度）
- 非常适合长序列处理

## 核心优势

| 优势 | 说明 |
|------|------|
| **长距离依赖** | 建模长序列能力接近 Transformer |
| **线性复杂度** | O(N) 而非 Transformer 的 O(N²) |
| **快速推理** | 适合实时/边缘部署 |
| **并行训练** | 支持高效训练 |

## SSM vs 其他架构

| 架构 | 长依赖 | 计算复杂度 | 推理速度 |
|------|--------|-----------|----------|
| Transformer | ✅ 极强 | O(N²) | 慢 |
| RNN | ⚠️ 弱 | O(N) | 快（但难训练） |
| **SSM (Mamba)** | ✅ 强 | **O(N)** | **快** |

## 在 SCMamba-YOLO 中的应用

- **Backbone**：用 Mamba 替代传统卷积/Attention
- **EGSSBlock**：将 SSM 与边界感知机制结合
- **目标**：兼顾精度和速度

## 相关概念

- [[concept-yolo]] — 目标检测框架
- [[entity-scmamba-yolo]] — SSM + YOLO 的结合体
- [[entity-egssblock]] — 边缘感知的 SSM 模块

---

*概念页由知识库自动生成*
