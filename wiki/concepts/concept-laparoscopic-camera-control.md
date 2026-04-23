---
title: Autonomous Laparoscopic Camera Control 腹腔镜相机自主控制
type: concept
created: 2026-04-12
updated: 2026-04-12
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
| **视野居中** | 让关键术野和器械保持在可观察区域 |
| **工作距离稳定** | 避免镜头过近或过远 |
| **减少抖动** | 提供平滑、舒适、可靠的视觉反馈 |
| **保证安全** | 满足器械运动和手术通道的几何约束 |

## 任务难点

- 器械运动快，容易造成相机跟随迟滞
- 手术场景存在遮挡、污染、起雾、组织变形
- 仅靠低层视觉误差容易产生抖动或不自然动作
- 相机运动需要同时满足可解释性和安全性

## 常见技术路线

| 路线 | 特点 |
|------|------|
| **传统视觉伺服** | 反应快，但通常偏反应式 |
| **学习式策略** | 能学习经验，但可解释性和安全性要求更高 |
| **语义策略 + 底层控制** | 高层理解任务语义，底层控制负责稳定执行 |

## 在 T-RO 论文中的体现

- 高层：VLM 判断当前主导 camera-handling strategy
- 中层：事件驱动图挖掘提供结构化策略原语
- 视觉前端：YOLOv26 + SAM2 视觉链路负责检测、细粒度分析与角度变化感知
- 底层：IBVS + RCM 控制器执行安全相机运动

## 相关页面

- [[concept-event-driven-graph-mining]] — 事件图策略挖掘
- [[concept-ibvs-rcm-control]] — 安全控制基础
- [[concept-yolov26-sam2-vision-pipeline]] — 主人负责的视觉算法链路
- [[source-2026-04-12-tro-laparoscopic-control]] — 对应论文

---

*概念页由知识库自动生成*
