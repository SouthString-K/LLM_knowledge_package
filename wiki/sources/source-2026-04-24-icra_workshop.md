---
title: "Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining"
type: source
created: 2026-04-24
updated: 2026-04-24
tags: [robotic-laparoscopy, autonomous-camera-control, event-driven-graph-mining, IBVS, RCM]
related:
  - concept-laparoscopic-camera-control
  - concept-event-driven-graph-mining
  - concept-ibvs-rcm-control
  - source-2026-04-12-tro-laparoscopic-control
confidence: high
source-ref:
  - raw/sources/papers_my_own/icra_workshop.pdf
aliases: ["icra_workshop", "Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining"]
---

# 资料摘要

这份 ICRA workshop 版本延续了腹腔镜自主持镜论文的核心路线：用事件驱动图挖掘抽取可复用的策略原语，再由高层视觉语言推理与低层 IBVS-RCM 控制共同完成相机运动决策。相比总论文版，这个版本更聚焦“strategy-grounded hierarchical control”这一主线，并明确给出离线策略发现与在线策略控制的两阶段框架。摘要中报告系统挖掘出 12 个可复用策略原语，并在离体实验中把 centering error 降低 35.26%、image shaking 降低 62.33%，适合作为该课题的短稿/展示版参考。

# 关键信息

- 论文方向：机器人微创手术中的腹腔镜自主相机控制
- 方法框架：离线事件解析与策略发现 + 在线 VLM 推理 + IBVS-RCM 执行
- 关键结果：12 个策略原语；centering error -35.26%；image shaking -62.33%
- 版本定位：更精炼的 workshop 版本，可作为 T-RO 主论文的配套材料

# 来源信息

- 原始文件：`raw/sources/papers_my_own/icra_workshop.pdf`

# 关联页面

- [[concept-laparoscopic-camera-control]] — 腹腔镜自主相机控制任务总览
- [[concept-event-driven-graph-mining]] — 事件图策略发现的核心方法
- [[concept-ibvs-rcm-control]] — 安全执行层的控制基础
- [[source-2026-04-12-tro-laparoscopic-control]] — 同题主论文版本

---

*本页由 ingest 工具生成后人工修订，作为腹腔镜自主持镜课题的 workshop 版本记录*
