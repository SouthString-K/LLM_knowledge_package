# 操作日志

> 格式：`## [日期] 操作类型 | 描述`

---

## 历史记录

## [2026-04-24] ingest | 新资料：Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining

**原始资料：** `raw/sources/papers_my_own/icra_workshop.pdf`

**资料页：** `source-2026-04-24-icra_workshop`

**自动关联页面：**
- source-2026-04-12-tro-laparoscopic-control
- source-2026-04-23-ocean-2026-04-14
- source-2026-04-24-mamba-yolo
- source-2026-04-12-scamba-yolo

**更新页面：**
- log.md
- index.md
- wiki/sources/source-2026-04-24-icra_workshop.md

## [2026-04-24] ingest | 新资料：Mamba YOLO: A Simple Baseline for Object Detection with State Space Model

**原始资料：** `raw/sources/paper_I_study/object_detection/Mamba-YOLO.pdf`

**资料页：** `source-2026-04-24-mamba-yolo`

**自动关联页面：**
- source-2026-04-12-scamba-yolo
- source-2026-04-12-tro-laparoscopic-control
- source-2026-04-23-ocean-2026-04-14
- source-2026-04-24-deimv2-dinov3

**更新页面：**
- log.md
- index.md
- wiki/sources/source-2026-04-24-mamba-yolo.md

## [2026-04-24] ingest | 新资料：Real-Time Object Detection Meets DINOv3

**原始资料：** `raw/sources/paper_I_study/object_detection/DEIMV2-DINOV3.pdf`

**资料页：** `source-2026-04-24-deimv2-dinov3`

**自动关联页面：**
- source-2026-04-12-tro-laparoscopic-control
- source-2026-04-12-scamba-yolo
- source-2026-04-24-deim
- source-2026-04-23-ocean-2026-04-14

**更新页面：**
- log.md
- index.md
- wiki/sources/source-2026-04-24-deimv2-dinov3.md

## [2026-04-24] ingest | 新资料：DEIM: DETR with Improved Matching for Fast Convergence

**原始资料：** `raw/sources/paper_I_study/object_detection/DEIM.pdf`

**资料页：** `source-2026-04-24-deim`

**自动关联页面：**
- source-2026-04-12-tro-laparoscopic-control
- source-2026-04-12-scamba-yolo
- source-2026-04-23-ocean-2026-04-14
- source-2026-04-24-第七版中国计算机学会推荐国际学术会议和期刊目录-正式版

**更新页面：**
- log.md
- index.md
- wiki/sources/source-2026-04-24-deim.md

## [2026-04-24] ingest | 新资料：中国计算机学会推荐国际学术会议和期刊目录

**原始资料：** `raw/sources/paper_I_study/第七版中国计算机学会推荐国际学术会议和期刊目录（正式版）.pdf`

**资料页：** `source-2026-04-24-第七版中国计算机学会推荐国际学术会议和期刊目录-正式版`

**自动关联页面：**
- source-2026-04-12-scamba-yolo
- source-2026-04-23-ocean-2026-04-14
- concept-object-detection
- concept-submarine-cable-detection

**更新页面：**
- log.md
- index.md
- wiki/sources/source-2026-04-24-第七版中国计算机学会推荐国际学术会议和期刊目录-正式版.md

## [2026-04-13] concept | 新建视觉算法链路概念页

- 新建概念页：concept-yolov26-sam2-vision-pipeline
- 内容聚焦：微调 YOLOv26 + SAM2 + 凸包角度计算
- 已关联到 T-RO 资料页与腹腔镜相机控制概念页
- 同步更新页面：index.md

## [2026-04-13] profile | 更新 T-RO 论文职责与创新点

- 在 PROFILE.md 中补充：负责 IEEE T-RO 腹腔镜相机自主控制论文的视觉算法部分
- 创新点更新为：微调 YOLOv26 + SAM2 + 凸包角度计算
- 补充性能信息：视觉链路帧率可达 30 fps
- 补充训练设定：多类别、多曝光、多环境微调训练
- 同步更新页面：wiki/sources/source-2026-04-12-tro-laparoscopic-control.md

## [2026-04-12] ingest | 论文：腹腔镜相机自主控制（T-RO）

**原始资料：** `raw/sources/papers_my_own/tro__Laparoscopic_control.pdf`

**论文信息：**
- 标题：Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining
- 目标期刊：IEEE Transactions on Robotics (T-RO)
- 核心路线：事件驱动图挖掘 + VLM 策略推断 + IBVS/RCM 安全控制

**涉及概念（新建3个）：**
- concept-laparoscopic-camera-control
- concept-event-driven-graph-mining
- concept-ibvs-rcm-control

**涉及资料页（新建1个）：**
- source-2026-04-12-tro-laparoscopic-control

**关键结果：**
- 标准化持镜评估优于 junior surgeons
- 视野居中误差降低 35%
- 图像抖动降低 62%

**矛盾标记：** 无

**更新页面：** index.md

## [2026-04-12] ingest | 论文：SCMamba-YOLO（第一篇）

**原始资料：** `raw/sources/papers_my_own/ocean.pdf`

**论文信息：**
- 标题：UW-Cable6K and SCMamba-YOLO: A Benchmark and Edge-Guided Mamba Framework for Submarine Cable Detection
- 会议：IEEE ICA Mal 2026
- 创新点：EGSSBlock（Edge-Guided State Space Block）

**涉及实体（新建2个）：**
- entity-scamba-yolo
- entity-egssblock

**涉及概念（新建4个）：**
- concept-state-space-models
- concept-yolo
- concept-object-detection
- concept-submarine-cable-detection

**涉及资料页（新建1个）：**
- source-2026-04-12-scamba-yolo

**矛盾标记：** 无

**更新页面：** index.md

---

## [2026-04-12] profile | 填写主人画像

- 身份：大二学生
- 研究方向：计算机视觉、机器人控制
- 技术栈：YOLO/DETR/RT-DETR/Mamba-YOLO、ROS2、机械臂
- 在投论文：ICA Mal 2026、YAC 2026、IEEE T-RO
- 画像已写入 PROFILE.md

---

*此文件由 LLM 自动维护，请勿手动修改*
