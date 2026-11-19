# FigureAtlas 图鉴

[English](README.md) | **中文说明**

> **300 种已经过截图验证的图，用于论文、幻灯片、海报和视频画面。**

[![图种](https://img.shields.io/badge/figures-300-blue.svg)](CATALOG.md)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Agent skill](https://img.shields.io/badge/Agent%20skill-ready-emerald.svg)](skills/visual-storyboard-designer/SKILL.md)

FigureAtlas 是一份给人看、也给编程智能体调用的图鉴。同一份结果经常要放进期刊栏、幻灯片和海报。图种只登记一次，画幅另外选择。

仓库原名是 Scientific Visual Studio。现在改成 `figureatlas`，读出来更短，搜索时也更不容易和别的 “visual studio” 混在一起。

## 里面有什么

- **300 种图**，分成 15 族。完整索引在 [CATALOG.md](CATALOG.md)。
- **每种图都有一张验证截图。** 截图先通过检查，再进入图库。[GALLERY.md](GALLERY.md) 展示的就是这些截图。
- **上一版的 26 个学科渲染器**仍然保留，包括布洛赫球、Bode 图、序列 logo、反应式和费曼图。
- **整个目录用同一个入口调用。**

```python
from figureatlas import render_figure
html = render_figure("161")  # 火山图
```

## 十五个图族

| 图族 | 数量 | 先看这些 |
|---|---:|---|
| 版式与跨媒介适配 | 18 | 期刊栏、16:9 幻灯片、A0 海报 |
| 分布、排序与组间比较 | 28 | 直方图、箱线图、森林图 |
| 相关、矩阵与降维 | 20 | 散点、热图、PCA |
| 时间、过程与实验序列 | 16 | 折线、Kaplan-Meier、甘特图 |
| 构成、集合与层级 | 14 | 矩形树图、维恩图、UpSet |
| 网络、流程与系统架构 | 25 | 桑基、时序、C4 |
| 数学、几何与推导 | 18 | 基底变换、斜率场、证明 |
| 机器学习结构与评测 | 20 | 混淆矩阵、SHAP、U-Net |
| 生命科学与组学 | 37 | 火山图、Circos、UMAP |
| 化学与材料 | 17 | 反应式、核磁、晶胞 |
| 物理、工程与信号 | 28 | Bode、史密斯圆图、波形 |
| 地图与空间 | 16 | 分级统计、流向、轨迹 |
| 科学插画与图形摘要 | 20 | 机制、装置、图形摘要 |
| 表格、代码与注释 | 8 | 三线表、代码块 |
| 医学临床与流行病 | 15 | CONSORT、游泳图、列线图 |

展示用截图在 `assets/gallery/atlas/`。验证时留下的副本在 `assets/gallery/_staging/`。

## 许可

[Apache 2.0](LICENSE)。
