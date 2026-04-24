---
title: "DEIM: DETR with Improved Matching for Fast Convergence"
type: source
created: 2026-04-24
updated: 2026-04-24
tags: [目标检测, DETR, 实时检测, 匹配策略, Dense-O2O]
related:
  - concept-object-detection
  - source-2026-04-24-deimv2-dinov3
  - source-2026-04-24-mamba-yolo
  - source-2026-04-12-scamba-yolo
confidence: high
source-ref:
  - raw/sources/paper_I_study/object_detection/DEIM.pdf
aliases: ["DEIM", "DEIM: DETR with Improved Matching for Fast Convergence"]
---

# 资料摘要

DEIM 针对 DETR 类实时检测器训练收敛慢、正样本稀疏的问题，引入 Dense O2O matching 和 Matchability-Aware Loss（MAL）来增加有效监督并抑制低质量匹配。论文报告该方法在 RT-DETR 和 D-FINE 上都能显著缩短训练时间，在 COCO 上把训练时间压缩约 50%。其中，基于 RT-DETRv2 的版本在单张 NVIDIA 4090 上 1 天训练即可达到 53.2 AP，而 DEIM-D-FINE-L / X 分别达到 54.7 / 56.5 AP，并在 T4 GPU 上实现 124 / 78 FPS，展示了很强的性能-效率平衡。

# 关键信息

- 核心问题：DETR 的 one-to-one matching 导致监督稀疏、训练收敛偏慢
- 关键方法：Dense O2O matching + Matchability-Aware Loss
- 代表结果：训练时间降低约 50%，RT-DETRv2 版本 1 天训练可达 53.2 AP
- 对比意义：为实时 DETR 路线提供了更可落地的训练范式

# 来源信息

- 原始文件：`raw/sources/paper_I_study/object_detection/DEIM.pdf`

# 关联页面

- [[concept-object-detection]] — 目标检测总览
- [[source-2026-04-24-deimv2-dinov3]] — DEIM 的后续扩展版本，引入 DINOv3 特征
- [[source-2026-04-24-mamba-yolo]] — 与 DEIM 一样关注实时检测的性能-效率平衡
- [[source-2026-04-12-scamba-yolo]] — 便于对比不同检测骨干与结构创新路线

---

*本页由 ingest 工具生成后人工修订，保留为实时 DETR 路线参考资料*
