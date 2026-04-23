---
title: Event-Driven Graph Mining 事件驱动图挖掘
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [事件建模, 图挖掘, 手术视频理解, 策略学习]
related:
  - concept-laparoscopic-camera-control
  - concept-ibvs-rcm-control
  - source-2026-04-12-tro-laparoscopic-control
confidence: high
aliases: ["Event-Driven Graph Mining", "事件图挖掘", "策略图挖掘"]
---

# 事件驱动图挖掘

## 概念定义

事件驱动图挖掘是指先把连续视频或任务流解析成有语义的离散事件，再把这些事件组织成图结构，从中发现高频模式、关键转移关系和可复用策略原语。

## 在手术相机控制中的意义

腹腔镜相机控制并不是单纯跟随工具点，而是要理解“当前发生了什么”。把手术视频转成事件图后，就能从专家行为中总结相机处理策略，而不是只拟合瞬时像素误差。

## T-RO 论文中的事件类型

- Tool-tissue interaction
- Working-distance deviation
- View-quality degradation

## 方法价值

| 价值 | 说明 |
|------|------|
| **结构化监督** | 把隐性的专家经验转成显式策略 |
| **可解释性** | 便于解释为什么当前要采取某种相机动作 |
| **可复用性** | 可沉淀为 strategy primitives，用于不同场景 |
| **连接高层与低层** | 让 VLM 推理和底层控制之间有中间语义层 |

## 与端到端控制的区别

| 方法 | 特点 |
|------|------|
| 端到端控制 | 直接从图像到动作，可能黑箱化 |
| **事件驱动图挖掘** | 先抽取事件和策略，再映射到动作，更可解释 |

## 相关页面

- [[concept-laparoscopic-camera-control]] — 应用任务
- [[concept-ibvs-rcm-control]] — 最终执行控制
- [[source-2026-04-12-tro-laparoscopic-control]] — 对应论文

---

*概念页由知识库自动生成*
