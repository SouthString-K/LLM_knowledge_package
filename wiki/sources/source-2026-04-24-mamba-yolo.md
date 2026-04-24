---
title: "Mamba YOLO: A Simple Baseline for Object Detection with State Space Model"
type: source
created: 2026-04-24
updated: 2026-04-24
tags: [目标检测, Mamba-YOLO, 状态空间模型, YOLO, 实时检测]
related:
  - concept-object-detection
  - concept-state-space-models
  - concept-yolo
  - source-2026-04-12-scamba-yolo
confidence: high
source-ref:
  - raw/sources/paper_I_study/object_detection/Mamba-YOLO.pdf
aliases: ["Mamba-YOLO", "Mamba YOLO: A Simple Baseline for Object Detection with State Space Model"]
---

# 资料摘要

Mamba-YOLO 把状态空间模型（SSM）引入 YOLO 风格的实时检测框架，试图用线性复杂度建模替代 Transformer 自注意力的二次复杂度。论文提出 ODMamba backbone 和 RG Block，在不依赖预训练的前提下提升全局建模与局部定位能力。作者报告其 tiny 版本在单张 4090 GPU 上可获得 7.5% mAP 提升，推理时间约 1.5 ms，强调了 SSM 路线在实时视觉任务中的效率优势。这篇材料也是理解后续 SCMamba-YOLO 的直接背景资料。

# 关键信息

- 核心目标：把 SSM 引入实时目标检测，降低自注意力带来的计算负担
- 关键模块：ODMamba backbone、RG Block
- 训练特点：强调“简单 baseline”，无需复杂预训练即可训练
- 代表结果：tiny 版本在单张 4090 上推理约 1.5 ms，并获得明显 mAP 提升

# 来源信息

- 原始文件：`raw/sources/paper_I_study/object_detection/Mamba-YOLO.pdf`

# 关联页面

- [[concept-object-detection]] — 目标检测总览
- [[concept-state-space-models]] — SSM / Mamba 的核心概念背景
- [[concept-yolo]] — YOLO 系列的主线框架
- [[source-2026-04-12-scamba-yolo]] — 在 Mamba-YOLO 基础上针对海缆检测做定制化增强

---

*本页由 ingest 工具生成后人工修订，保留为 SSM 检测路线背景资料*
