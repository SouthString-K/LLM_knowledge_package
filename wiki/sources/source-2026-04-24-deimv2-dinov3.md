---
title: "Real-Time Object Detection Meets DINOv3"
type: source
created: 2026-04-24
updated: 2026-04-24
tags: [目标检测, DINOv3, DETR, 实时检测, 轻量化]
related:
  - concept-object-detection
  - source-2026-04-24-deim
  - source-2026-04-24-mamba-yolo
  - concept-yolo
confidence: high
source-ref:
  - raw/sources/paper_I_study/object_detection/DEIMV2-DINOV3.pdf
aliases: ["DEIMV2-DINOV3", "Real-Time Object Detection Meets DINOv3"]
---

# 资料摘要

这篇工作把 DINOv3 特征引入实时目标检测，形成 DEIMv2，并用 Spatial Tuning Adapter（STA）把 DINOv3 的单尺度语义特征转成适合检测器的多尺度表示。论文统一覆盖从 X 到 Atto 的 8 个模型尺寸，兼顾 GPU、边缘和移动端部署。关键结果包括：DEIMv2-X 在仅 50.3M 参数下达到 57.8 AP；DEIMv2-S 以 9.71M 参数首次让 sub-10M 模型超过 50 AP；而 1.5M 参数的 Pico 版本达到 38.5 AP，显示出很强的轻量化潜力。

# 关键信息

- 核心思路：用 DINOv3 预训练表征增强实时检测器
- 关键组件：Spatial Tuning Adapter（STA）+ 升级版 Dense O2O
- 模型范围：从 X / L / M / S 到 Nano / Pico / Femto / Atto
- 代表结果：57.8 AP（X 版），50.9 AP（S 版），38.5 AP（Pico）

# 来源信息

- 原始文件：`raw/sources/paper_I_study/object_detection/DEIMV2-DINOV3.pdf`

# 关联页面

- [[concept-object-detection]] — 目标检测总览
- [[source-2026-04-24-deim]] — 方法论前作，提供 Dense O2O 训练基础
- [[source-2026-04-24-mamba-yolo]] — 可作为实时检测器不同技术路线的对照材料
- [[concept-yolo]] — 便于对照 YOLO 与 DETR 路线在实时检测上的不同取舍

---

*本页由 ingest 工具生成后人工修订，保留为实时检测与视觉骨干设计参考资料*
