# BLADE Slides｜高保真可编辑 PPT 还原

**中文优先阅读：** [完整中文 Skill](SKILL.zh-CN.md) · [English Skill](SKILL.md) · [中文参考资料导航](references/README.zh-CN.md) · [更新记录](CHANGELOG.md)

> 从获认可的幻灯片图片、截图、图片型 PPTX/PDF，还原为**高保真、接近人工制作习惯、可实际编辑**的 PowerPoint。

**BLADE = Bao Layered Asset Decomposition & Editability for PowerPoint**。

先用图像方式制作 PPT，往往能得到很好的视觉效果；但最终页面通常会变成一张平面图。BLADE 提供一套 Agent 工作流、图层契约和确定性 QA 脚本，把已验收设计还原成实用的 PowerPoint 图层系统。

它的目标不是“把每一个像素都矢量化”，而是在不牺牲获认可的视觉品质前提下，让人真正需要调整的文字、模块和规则图形，像人工制作的 PPT 一样可理解、可移动、可复用。

## 中文用户从这里开始

1. 阅读 [SKILL.zh-CN.md](SKILL.zh-CN.md)，了解完整工作流、可编辑边界和最终 QA。
2. 运行 `scripts/init_layer_contract.py`，先决定哪些对象应移动、哪些必须保留为高保真复合视觉。
3. 逐页构建与验证，不要直接把整页图片叠加可编辑文字。
4. 交付前运行 `validate_layer_contract.py`、`audit_human_editability.py`，并在真实 Microsoft PowerPoint 中打开、保存、重开与导出。

参考材料均配有中文说明：

| 主题 | 中文资料 |
| --- | --- |
| 方法与图层拆分 | [methodology.zh-CN.md](references/methodology.zh-CN.md) |
| 人类可编辑性标准 | [human-editability.zh-CN.md](references/human-editability.zh-CN.md) |
| 页面交付契约 | [page-worker-contract.zh-CN.md](references/page-worker-contract.zh-CN.md) |
| QA 关卡 | [qa-gates.zh-CN.md](references/qa-gates.zh-CN.md) |
| 常见失败与修复 | [failure-modes.zh-CN.md](references/failure-modes.zh-CN.md) |
| ImageGen 提示词模式 | [imagegen-prompts.zh-CN.md](references/imagegen-prompts.zh-CN.md) |

## BLADE 会重建什么

- 可读的商业文字，作为原生 PowerPoint 文本；
- 普通卡片、边框、坐标轴、连接线和分割线，作为原生形状；
- 图标、圆章、金属节点、玻璃和光效，作为干净、可移动的透明资产；
- 与透视、人物或场景材质强绑定的复杂视觉，作为有明确说明的固定场景元素；
- 带有语义化 Selection Pane 名称的完整模块；
- 当前景元素移走后，仍然自然完整的干净背景。

## BLADE 明确拒绝什么

- 整页截图上方只叠可编辑文字；
- 用数百张极小图片切片伪装可编辑几何；
- 整套 deck 充满 `Image 37`、`TextBox 22` 这类无意义对象名；
- 不完整的边框、被切掉的圆形、带底图污染的透明资产、或移动后露出第二个对象；
- 大部分设计仍是一张未披露平面图，却被称为“完全可编辑”的文件。

## 仓库内容

```text
blade-slides/
|-- README.md                    # 中英双语介绍入口
|-- SKILL.md                     # English workflow instructions
|-- SKILL.zh-CN.md               # 完整中文工作说明
|-- agents/openai.yaml           # 双语界面元数据
|-- assets/layer-contract-template.json
|-- references/                  # English references + 中文对应资料
|-- scripts/
|   |-- init_layer_contract.py
|   |-- validate_layer_contract.py
|   |-- audit_human_editability.py
|   `-- self_check.py
`-- requirements.txt
```

## 环境要求与安装

需要：能读取 skill/instruction 目录的 AI Agent、Python 3.10+、Pillow、python-pptx；用于处理干净底图与透明素材的图像编辑或生成能力；以及用于最终验收的真实 Microsoft PowerPoint。

打包脚本跨平台，但“无 Repair 打开且正确导出”的最终关卡必须在真实 Microsoft PowerPoint 中完成；只用库或其他办公套件测试并不等价。

### Codex 安装示例

```bash
git clone https://github.com/bryanbao-lab/blade-slides.git ~/.codex/skills/blade-slides
python3 -m pip install -r ~/.codex/skills/blade-slides/requirements.txt
```

然后调用：

```text
请使用 $blade-slides 将这张已获认可的幻灯片图片还原为高保真、可实际编辑的 PowerPoint。
文字保持原生可编辑，规则模块独立可移动；必要时保留复杂视觉为干净的高保真复合图层。
```

### 其他 Agent 平台

将仓库克隆或复制到平台的 skill/instruction 目录，并命名为 `blade-slides`。若平台忽略 YAML front matter，直接提供 `SKILL.md` 或中文场景下的 `SKILL.zh-CN.md`；同时保留 `references/`、`scripts/` 与 `assets/` 的相对路径。

## 快速开始

创建图层契约：

```bash
python3 scripts/init_layer_contract.py \
  --slide-id slide_01 \
  --source /absolute/path/source.png \
  --out /absolute/path/layer_contract.json \
  --mode full_rebuild
```

根据源图填写 contract 后，验证重建页面：

```bash
python3 scripts/validate_layer_contract.py \
  /absolute/path/layer_contract.json \
  --pptx /absolute/path/page.pptx \
  --report /absolute/path/validation.json
```

对整套 deck 审核“伪可编辑”问题：

```bash
python3 scripts/audit_human_editability.py \
  /absolute/path/final.pptx \
  --strict \
  --report /absolute/path/human_editability.json
```

运行本地自检：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/self_check.py
```

## 生产模式与图层类型

| 模式 | 含义 |
| --- | --- |
| `full_rebuild` | 重建新页面或完整图片化 deck |
| `local_refinement` | 只调整已验收 deck 中指定页面或模块 |
| `review_draft` | 快速临时审阅文件；绝不能称为 BLADE final |

| 类型 | 含义 |
| --- | --- |
| `clean_base` | 移走可移动元素后仍自然的背景 |
| `native_text` | 可编辑文本 |
| `native_shape` | 安全、规则的 PowerPoint 几何 |
| `transparent_png` | 可移动、保真度高的复杂视觉资产 |
| `fixed_scene_visual` | 为保真而有意固定的场景绑定视觉 |

## 如实说明可编辑边界

BLADE 是**保真优先的分层可编辑**，不是自动的全量矢量化。

光学玻璃、金属材质、摄影、复杂光路、粒子网络，以及和建筑/人物/透视强绑定的视觉，通常应保留为高品质栅格复合体。最终交付必须明确：哪些对象为原生文本或形状、哪些为可移动透明资产、哪些为保真固定元素。

## 隐私与公开安全

本仓库不包含客户演示稿、公司机密设计或文案、私有 Logo 或源图、用户本机路径、API Key、Token、凭据、OCR 输出，或由私有 deck 生成的生产 QA 报告。示例均为通用内容。

除非你拥有公开权利，否则不要提交源演示稿、提取媒体、clean base、截图或审阅证据，也不要提交非官方的企业 Logo 副本。

## 参与贡献

欢迎提交 bug report 和 pull request。特别欢迎：更多 PowerPoint 结构检查、更可靠的透明/边缘完整性诊断、采用宽松授权素材的可复现公开示例，以及跨平台的 Microsoft PowerPoint 自动化说明。

## English

**Turn finished slide images into source-faithful, human-editable PowerPoint.**

BLADE turns an approved flat slide design into a practical layer system instead of merely placing editable text over a screenshot. It preserves visual quality while making the elements a human actually needs to adjust meaningful, movable, and reusable.

Start with [SKILL.md](SKILL.md). The core workflow is:

1. classify every visible object with a layer contract;
2. rebuild readable copy as native text and regular geometry as native shapes;
3. retain complex materials as clean meaningful transparent composites or documented fixed scene visuals;
4. prove clean-base exclusivity and move-away behavior;
5. validate in real Microsoft PowerPoint, then record final QA and checksum.

The same repository includes full English references and corresponding Chinese guides. See [references/README.zh-CN.md](references/README.zh-CN.md) for the Chinese reference map.

## Author and license

Created by [Bryan Bao](https://github.com/bryanbao-lab). Released under the [MIT License](LICENSE).

## Version

**V2.1.1** refines material-aware decomposition, composited glass-opacity checks, and same-slide object protection. This is a bilingual guidance patch; scripts and schemas are unchanged. / 本次补丁完善材质优先判断、玻璃叠层透明度检查及同页对象保护；中英文同步，脚本和 schema 不变。

**V2.1.0** adds a Chinese-first bilingual README, a complete Chinese skill guide, Chinese reference guides, and bilingual UI metadata. The underlying public-safe workflow and deterministic scripts remain compatible with V2.0.0.
