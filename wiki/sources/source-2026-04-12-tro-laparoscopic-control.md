---
title: "Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining"
type: source
created: 2026-04-12
updated: 2026-04-12
tags: [robotic-laparoscopy, autonomous-camera-control, event-driven-graph-mining, IBVS, RCM, VLM]
related:
  - concept-laparoscopic-camera-control
  - concept-event-driven-graph-mining
  - concept-ibvs-rcm-control
  - concept-yolov26-sam2-vision-pipeline
confidence: high
source-ref:
  - raw/sources/papers_my_own/Strategy_Supervised_Autonomous_Laparoscopic_Camera_Control_via_Event_Driven_Graph_Mining.pdf
aliases: ["T-RO腹腔镜相机控制论文", "Laparoscopic Camera Control", "Event-Driven Graph Mining Camera Control"]
---

# 论文摘要

This paper studies autonomous laparoscopic camera control for robotic minimally invasive surgery. The proposed framework combines offline event-driven graph mining with online vision-language-guided control. Surgical videos are parsed into camera-relevant temporal events such as tool-tissue interaction, working-distance deviation, and view-quality degradation, then organized into attributed event graphs to mine reusable camera-handling strategy primitives. Online, a fine-tuned Vision-Language Model predicts the dominant strategy and discrete image-based motion commands, which are executed by an IBVS controller under RCM and safety constraints. Ex vivo experiments on silicone phantoms and porcine tissues show that the system outperforms junior surgeons in standardized camera-handling evaluation, reducing field-of-view centering error by 35% and image shaking by 62% while preserving smooth motion and stable working distance.

# 关键信息

## 论文信息

| 项目 | 内容 |
|------|------|
| 标题 | Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining |
| 期刊/目标 | IEEE Transactions on Robotics (T-RO) |
| 状态 | 在投 |
| 时间线 | PDF 元数据创建于 2026-02-17 |

## 核心思路

| 模块 | 描述 |
|------|------|
| **离线事件解析** | 从腹腔镜视频中提取相机相关事件 |
| **事件图挖掘** | 将事件组织为 attributed event graph，挖掘可复用策略原语 |
| **在线策略推断** | 微调 Vision-Language Model 预测当前主导策略与离散图像运动指令 |
| **安全执行控制** | 用 IBVS + RCM 约束控制器执行相机运动 |

## 主人负责的视觉算法部分

| 模块 | 描述 |
|------|------|
| **YOLOv26 先验检测** | 使用自我微调的 YOLOv26 作为先验知识提取器 |
| **鲁棒训练** | 针对多类别、多曝光、多环境数据进行微调训练 |
| **SAM2 细粒度分析** | 在检测结果基础上进一步做细粒度区域与结构分析 |
| **角度变化检测** | 使用凸包算法进行角度运算，精准检测角度变化 |
| **实时性** | 视觉处理链路帧率可达到 30 fps |

## 关键事件类型

- Tool-tissue interaction
- Working-distance deviation
- View-quality degradation

## 实验结论

| 指标/现象 | 结果 |
|------|------|
| 标准化相机持镜评估 | 优于 junior surgeons |
| Field-of-view centering error | 降低 35% |
| Image shaking | 降低 62% |
| 运动品质 | 保持平滑运动与稳定工作距离 |

## 方法亮点

1. 将“相机控制”从纯反应式视觉伺服提升为带有语义策略层的控制问题
2. 用事件驱动图挖掘从手术视频中提炼结构化 supervision
3. 将 VLM 的高层理解与 IBVS/RCM 的低层安全控制耦合
4. 视觉前端采用 **YOLOv26（微调）+ SAM2** 联合框架，实现高速检测与细粒度分析结合
5. 利用 **凸包算法** 精准计算角度变化，增强几何状态感知能力
6. 支持 speech input，形成 human-in-the-loop 条件控制

## 相关概念

- [[concept-laparoscopic-camera-control]] — 腹腔镜相机自主控制任务
- [[concept-event-driven-graph-mining]] — 从事件图中挖掘可复用策略
- [[concept-ibvs-rcm-control]] — 图像视觉伺服与 RCM 安全约束
- [[concept-yolov26-sam2-vision-pipeline]] — YOLOv26 + SAM2 + 凸包角度计算视觉链路

---

*本页由 LLM 自动生成，内容来自原始论文 PDF 抽取与整理*
