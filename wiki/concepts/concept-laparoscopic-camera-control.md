---
title: Autonomous Laparoscopic Camera Control 腹腔镜相机自主控制
type: concept
created: 2026-04-12
updated: 2026-04-24
tags: [机器人手术, 腹腔镜, 相机控制, 医疗机器人]
related:
  - concept-ibvs-rcm-control
  - concept-event-driven-graph-mining
  - concept-yolov26-sam2-vision-pipeline
  - source-2026-04-12-tro-laparoscopic-control
confidence: high
aliases: ["Autonomous Laparoscopic Camera Control", "腹腔镜持镜控制", "腹腔镜相机自主控制"]
---

# 腹腔镜相机自主控制

## 概念定义

腹腔镜相机自主控制是指让机器人在微创手术过程中自动调整相机视角、中心、距离和稳定性，以持续提供安全、清晰、可操作的手术视野。

## 任务目标

| 目标 | 说明 |
|------|------|
| 视野居中 | 让关键术野和器械保持在可观察区域 |
| 工作距离稳定 | 避免镜头过近或过远 |
| 减少抖动 | 提供平滑、可靠的视觉反馈 |
| 保证安全 | 满足器械运动和手术通道的几何约束 |

## 当前课题中的技术路线

- 高层：VLM 判断当前主导 camera-handling strategy
- 中层：事件驱动图挖掘提供结构化策略原语
- 视觉前端：YOLOv26 + SAM2 链路负责检测、细粒度分析与角度变化感知
- 低层：IBVS + RCM 控制器执行安全相机运动

## 新增关联资料

- [[source-2026-04-24-icra_workshop]] — 同一课题的 workshop 版本，突出策略原语与层级控制框架

## 相关页面

- [[concept-event-driven-graph-mining]] — 事件图策略发现
- [[concept-ibvs-rcm-control]] — 安全控制基础
- [[concept-yolov26-sam2-vision-pipeline]] — 视觉算法链路
- [[source-2026-04-12-tro-laparoscopic-control]] — 对应主论文版本

---

*概念页由知识库自动生成后持续增量维护*
