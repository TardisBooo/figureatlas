# FigureAtlas 图鉴

[English](README.md) | **中文说明**

> **300 种已经过截图验证的图，用于论文、幻灯片、海报和视频画面。**

[![图种](https://img.shields.io/badge/figures-300-blue.svg)](CATALOG.md)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Agent skill](https://img.shields.io/badge/Agent%20skill-ready-emerald.svg)](skills/visual-storyboard-designer/SKILL.md)

FigureAtlas 是一份给人看、也给编程智能体调用的图鉴。同一份结果经常要放进期刊栏、幻灯片和海报。图种只登记一次，画幅另外选择。

仓库原名是 Scientific Visual Studio。现在改成 `figureatlas`，读出来更短，搜索时也更不容易和别的 “visual studio” 混在一起。

The English page is [README.md](README.md). This page keeps the same 30 figures, with Chinese titles.

## 里面有什么

- **300 种图**，分成 15 族。完整索引在 [CATALOG.md](CATALOG.md)。
- **每种图都有一张验证截图。** 截图先通过检查，再进入图库。完整展示在 [GALLERY.md](GALLERY.md)。
- **上一版的 26 个学科渲染器**仍然保留，包括布洛赫球、Bode 图、序列 logo、反应式和费曼图。
- **整个目录用同一个入口调用。**

```python
from figureatlas import render_figure
html = render_figure("161")  # 火山图
```

DeepSeek Harness 的安装清单在 `package.json` 的 `dsh.bundle`，技能注册写在 `cordis.patch.yml`。

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

## 图库

下面是 30 张已经通过检查的图。另外 270 张在 [GALLERY.md](GALLERY.md)。点图片可以打开对应的 HTML。

| | |
|:---:|:---:|
| <div align="center"><b>001 电影级封面</b><br/><a href="assets/gallery/atlas/001_hero-cover.html"><img src="assets/gallery/atlas/001_hero-cover.png" width="360" alt="Cinematic title cover"/></a><br/><sub>Cinematic title cover</sub></div> | <div align="center"><b>011 A0 海报模块</b><br/><a href="assets/gallery/atlas/011_poster-a0.html"><img src="assets/gallery/atlas/011_poster-a0.png" width="360" alt="A0 poster module"/></a><br/><sub>A0 poster module</sub></div> |
| <div align="center"><b>022 密度曲线</b><br/><a href="assets/gallery/atlas/022_density.html"><img src="assets/gallery/atlas/022_density.png" width="360" alt="Density curve"/></a><br/><sub>Density curve</sub></div> | <div align="center"><b>032 堆叠柱状图</b><br/><a href="assets/gallery/atlas/032_stacked-bar.html"><img src="assets/gallery/atlas/032_stacked-bar.png" width="360" alt="Stacked bars"/></a><br/><sub>Stacked bars</sub></div> |
| <div align="center"><b>042 森林图</b><br/><a href="assets/gallery/atlas/042_forest.html"><img src="assets/gallery/atlas/042_forest.png" width="360" alt="Forest plot"/></a><br/><sub>Forest plot</sub></div> | <div align="center"><b>053 聚类热图</b><br/><a href="assets/gallery/atlas/053_cluster-heat.html"><img src="assets/gallery/atlas/053_cluster-heat.png" width="360" alt="Clustered heatmap"/></a><br/><sub>Clustered heatmap</sub></div> |
| <div align="center"><b>063 ROC 曲线</b><br/><a href="assets/gallery/atlas/063_roc.html"><img src="assets/gallery/atlas/063_roc.png" width="360" alt="ROC curve"/></a><br/><sub>ROC curve</sub></div> | <div align="center"><b>073 火花线</b><br/><a href="assets/gallery/atlas/073_sparkline.html"><img src="assets/gallery/atlas/073_sparkline.png" width="360" alt="Sparkline row"/></a><br/><sub>Sparkline row</sub></div> |
| <div align="center"><b>083 饼图</b><br/><a href="assets/gallery/atlas/083_pie.html"><img src="assets/gallery/atlas/083_pie.png" width="360" alt="Pie chart"/></a><br/><sub>Pie chart</sub></div> | <div align="center"><b>094 欧拉图</b><br/><a href="assets/gallery/atlas/094_euler.html"><img src="assets/gallery/atlas/094_euler.png" width="360" alt="Euler diagram"/></a><br/><sub>Euler diagram</sub></div> |
| <div align="center"><b>104 邻接矩阵</b><br/><a href="assets/gallery/atlas/104_adj-matrix.html"><img src="assets/gallery/atlas/104_adj-matrix.png" width="360" alt="Adjacency matrix"/></a><br/><sub>Adjacency matrix</sub></div> | <div align="center"><b>114 C4 组件</b><br/><a href="assets/gallery/atlas/114_c4-component.html"><img src="assets/gallery/atlas/114_c4-component.png" width="360" alt="C4 component"/></a><br/><sub>C4 component</sub></div> |
| <div align="center"><b>125 复平面</b><br/><a href="assets/gallery/atlas/125_complex-plane.html"><img src="assets/gallery/atlas/125_complex-plane.png" width="360" alt="Complex plane"/></a><br/><sub>Complex plane</sub></div> | <div align="center"><b>135 卷积滑窗</b><br/><a href="assets/gallery/atlas/135_convolution.html"><img src="assets/gallery/atlas/135_convolution.png" width="360" alt="Convolution window"/></a><br/><sub>Convolution window</sub></div> |
| <div align="center"><b>145 学习曲线</b><br/><a href="assets/gallery/atlas/145_learning-curve.html"><img src="assets/gallery/atlas/145_learning-curve.png" width="360" alt="Learning curve"/></a><br/><sub>Learning curve</sub></div> | <div align="center"><b>156 词元流向</b><br/><a href="assets/gallery/atlas/156_token-flow.html"><img src="assets/gallery/atlas/156_token-flow.png" width="360" alt="Token flow"/></a><br/><sub>Token flow</sub></div> |
| <div align="center"><b>166 富集条形</b><br/><a href="assets/gallery/atlas/166_enrich-bar.html"><img src="assets/gallery/atlas/166_enrich-bar.png" width="360" alt="Enrichment bars"/></a><br/><sub>Enrichment bars</sub></div> | <div align="center"><b>176 单细胞 UMAP 分群</b><br/><a href="assets/gallery/atlas/176_sc-umap.html"><img src="assets/gallery/atlas/176_sc-umap.png" width="360" alt="Single-cell UMAP"/></a><br/><sub>Single-cell UMAP</sub></div> |
| <div align="center"><b>187 PCoA / NMDS</b><br/><a href="assets/gallery/atlas/187_pcoa.html"><img src="assets/gallery/atlas/187_pcoa.png" width="360" alt="PCoA / NMDS"/></a><br/><sub>PCoA / NMDS</sub></div> | <div align="center"><b>197 二维分子反应式</b><br/><a href="assets/gallery/atlas/197_reaction-scheme.html"><img src="assets/gallery/atlas/197_reaction-scheme.png" width="360" alt="Reaction scheme"/></a><br/><sub>Reaction scheme</sub></div> |
| <div align="center"><b>207 XRD</b><br/><a href="assets/gallery/atlas/207_xrd.html"><img src="assets/gallery/atlas/207_xrd.png" width="360" alt="Powder XRD"/></a><br/><sub>Powder XRD</sub></div> | <div align="center"><b>218 Bode / Nyquist</b><br/><a href="assets/gallery/atlas/218_bode-nyquist.html"><img src="assets/gallery/atlas/218_bode-nyquist.png" width="360" alt="Bode and Nyquist"/></a><br/><sub>Bode and Nyquist</sub></div> |
| <div align="center"><b>228 小波尺度图</b><br/><a href="assets/gallery/atlas/228_scalogram.html"><img src="assets/gallery/atlas/228_scalogram.png" width="360" alt="Wavelet scalogram"/></a><br/><sub>Wavelet scalogram</sub></div> | <div align="center"><b>238 机架图</b><br/><a href="assets/gallery/atlas/238_rack.html"><img src="assets/gallery/atlas/238_rack.png" width="360" alt="Rack elevation"/></a><br/><sub>Rack elevation</sub></div> |
| <div align="center"><b>248 等值线地图</b><br/><a href="assets/gallery/atlas/248_iso-map.html"><img src="assets/gallery/atlas/248_iso-map.png" width="360" alt="Isoline map"/></a><br/><sub>Isoline map</sub></div> | <div align="center"><b>259 源码与内存双栏</b><br/><a href="assets/gallery/atlas/259_code-inspector.html"><img src="assets/gallery/atlas/259_code-inspector.png" width="360" alt="Code and memory inspector"/></a><br/><sub>Code and memory inspector</sub></div> |
| <div align="center"><b>269 图形摘要四格</b><br/><a href="assets/gallery/atlas/269_abstract-quad.html"><img src="assets/gallery/atlas/269_abstract-quad.png" width="360" alt="Graphical abstract quad"/></a><br/><sub>Graphical abstract quad</sub></div> | <div align="center"><b>279 回归系数表</b><br/><a href="assets/gallery/atlas/279_coef-table.html"><img src="assets/gallery/atlas/279_coef-table.png" width="360" alt="Coefficient table"/></a><br/><sub>Coefficient table</sub></div> |
| <div align="center"><b>290 列线图</b><br/><a href="assets/gallery/atlas/290_nomogram.html"><img src="assets/gallery/atlas/290_nomogram.png" width="360" alt="Nomogram"/></a><br/><sub>Nomogram</sub></div> | <div align="center"><b>300 网状荟萃联赛表</b><br/><a href="assets/gallery/atlas/300_league-table.html"><img src="assets/gallery/atlas/300_league-table.png" width="360" alt="Network meta-analysis league"/></a><br/><sub>Network meta-analysis league</sub></div> |

展示用截图在 `assets/gallery/atlas/`。验证时留下的副本在 `assets/gallery/_staging/`。

## 许可

[Apache 2.0](LICENSE)。
