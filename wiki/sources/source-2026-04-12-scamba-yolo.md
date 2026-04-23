---
title: "UW-Cable6K and SCMamba-YOLO: A Benchmark and Edge-Guided Mamba Framework for Submarine Cable Detection"
type: source
created: 2026-04-12
updated: 2026-04-12
tags: [Mamba-YOLO, submarine-cable-detection, object-detection, EGSSBlock, benchmark]
related:
  - entity-scmamba-yolo
  - entity-egssblock
  - concept-state-space-models
  - concept-yolo
confidence: high
source-ref:
  - raw/sources/papers_my_own/ocean.pdf
aliases: ["SCMamba-YOLO", "UW-Cable6K海缆检测"]
---

# 论文摘要

Submarine cable detection is essential for automated maritime monitoring, yet remains challenging due to underwater degradation and slender target morphology. This paper proposes SCMamba-YOLO, featuring an EGSSBlock designed to enhance boundary perception and structural continuity. Evaluations on our UW-Cable6K benchmark show that the model achieves **98.8% AP50, 88.5% AP75, and 78.3% AP50:95**. These results outperform existing object detection baselines with a low inference latency of **6.0 ms**. The proposed framework provides an efficient solution for autonomous transportation and real-time subsea infrastructure maintenance in complex maritime environments.

# 关键信息

## 论文信息

| 项目 | 内容 |
|------|------|
| 标题 | UW-Cable6K and SCMamba-YOLO: A Benchmark and Edge-Guided Mamba Framework for Submarine Cable Detection |
| 会议 | IEEE ICA Mal 2026 |
| 状态 | 在投 |
| 发表时间 | 2026 |

## 核心创新

| 创新点 | 描述 |
|--------|------|
| **EGSSBlock** | Edge-Guided State Space Block，增强边界感知和结构连续性 |
| **UW-Cable6K** | 自建水下海缆检测基准数据集 |
| **SCMamba-YOLO** | 将 Mamba 状态空间模型与 YOLO 架构结合 |

## 核心性能指标

| 指标 | 值 |
|------|---|
| AP50 | 98.8% |
| AP75 | 88.5% |
| AP50:95 | 78.3% |
| 推理延迟 | 6.0 ms |

## 技术关键词

- Submarine Cable Detection（水下海缆检测）
- State Space Models（状态空间模型）
- Mamba
- YOLO
- Edge-Guided Detection（边界引导检测）
- Automated Monitoring（自动化监测）
- Autonomous Transportation（自动驾驶运输）

## 研究背景

- **任务挑战**：水下图像退化 + 细长目标形态 → 海缆检测困难
- **应用场景**：海上自动化监控、海底基础设施维护

## 方法亮点

1. **EGSSBlock**：专为海缆识别任务设计，增强边界感知和结构连续性
2. **轻量化推理**：6.0ms 低延迟，适合实时检测
3. **自建基准**：UW-Cable6K 水下海缆数据集

---

*本页由 LLM 自动生成，内容来自原始论文摘要*
