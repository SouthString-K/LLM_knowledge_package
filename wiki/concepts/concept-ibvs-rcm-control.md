---
title: IBVS + RCM Control 图像视觉伺服与 RCM 约束控制
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [IBVS, RCM, 视觉伺服, 机器人控制, 医疗机器人]
related:
  - concept-laparoscopic-camera-control
  - concept-event-driven-graph-mining
  - source-2026-04-12-tro-laparoscopic-control
confidence: high
aliases: ["IBVS", "RCM", "Image-Based Visual Servoing", "Remote Center of Motion"]
---

# 图像视觉伺服与 RCM 约束控制

## 概念定义

IBVS（Image-Based Visual Servoing）是利用图像平面中的误差直接驱动机器人运动的控制方法；RCM（Remote Center of Motion）则是微创手术器械必须满足的关键几何约束，要求器械绕 trocar/切口附近的固定中心运动，避免造成额外组织损伤。

## 为什么两者要结合

在腹腔镜场景里，仅有 IBVS 不够，因为相机虽然能追踪图像目标，但仍可能违反手术器械的安全运动约束；加入 RCM 后，控制器才能在“看得准”和“动得安全”之间取得平衡。

## 核心作用

| 模块 | 作用 |
|------|------|
| **IBVS** | 根据图像误差调整相机方向、位置和视野中心 |
| **RCM** | 保证器械/镜头运动满足手术入口约束 |
| **Safety constraints** | 限制不合理速度、姿态和危险动作 |

## 在 T-RO 论文中的角色

- VLM 输出高层策略与离散图像运动命令
- IBVS + RCM 控制器负责把这些命令变成连续、安全、平滑的机器人动作
- 形成“高层语义策略 + 低层安全控制”的闭环

## 方法特征

- 比纯语义决策更稳定
- 比纯反应式视觉伺服更理解上下文
- 适合用于 human-in-the-loop 的医疗机器人系统

## 相关页面

- [[concept-laparoscopic-camera-control]] — 应用任务
- [[concept-event-driven-graph-mining]] — 高层策略来源
- [[source-2026-04-12-tro-laparoscopic-control]] — 对应论文

---

*概念页由知识库自动生成*
