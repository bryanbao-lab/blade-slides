---
name: blade-slides
language: zh-CN
version: "2.1.0"
---

# BLADE Slides V2.1.0｜高保真可编辑 PPT 分层还原

**BLADE = Bao Layered Asset Decomposition & Editability for PowerPoint**。

BLADE 的目标不是把整页图片上方强行叠一层“可改文字”，而是把已获认可的设计还原成接近人工制作习惯的 PowerPoint 图层系统：对象有意义、模块能独立移动、规则几何可编辑、复杂质感不被廉价重画；移动前景后，底图也应自然完整。

质量优先级：**源图保真 > 人类可编辑性 > PowerPoint 稳定性 > 速度**。不得用“快速转换”掩盖碎片化、错位、像素污染或难以理解的图层关系。

本文件是 [SKILL.md](SKILL.md) 的中文完整工作说明；英文原文适合英文 Agent 读取，中文版本面向中文用户、中文团队与审阅者。

## 所需能力

使用当前环境中最合适的工具完成：

- 源图检查、OCR、局部裁切对比与透明 alpha 检查；
- 图像编辑或生成，以制作干净底图和隔离透明资产；
- 原生 PowerPoint 构建或保守的 OOXML 编辑；
- 真实官方 Logo 与品牌资产检索；
- 真实 Microsoft PowerPoint 最终验证。

若项目提供治理文件、视觉规范、可信模板或已验收的可编辑基线，必须先读取并遵守。

## 三种生产模式

在创建素材前，先在 layer contract 中只选择一种模式。

### `full_rebuild`

从扁平设计稿重建新页面或整批页面。每页独立构建和验证，再合并。

### `local_refinement`

在已验收的 BLADE deck 上做局部修正，不能重做已经成功的页面。记录：

- `accepted_baseline.source_deck`
- `allowed_change_slides`
- `protected_slides`
- 用于保护未修改页面的渲染或结构对比方法。

可以使用保守的 OOXML 或库级补丁，但最终文件仍须由真实 Microsoft PowerPoint 打开、保存、重新打开和导出。

### `review_draft`

用于快速内容审阅的临时文件，例如全页底图上叠加可编辑文字。它**不是** BLADE final；文件名和交付说明必须写明 `REVIEW_DRAFT`，不得声称为完整分层可编辑稿。

## 先冻结图层契约

在生成任何资产之前建立 contract：

```bash
python3 <skill-directory>/scripts/init_layer_contract.py \
  --slide-id slide_07 \
  --source /absolute/path/source.png \
  --out /absolute/path/layer_contract.json \
  --mode full_rebuild
```

每个可见元素只能选一种表达方式：

| 类型 | 适用内容 |
| --- | --- |
| `clean_base` | 移除所有可移动对象后仍自然的场景底图 |
| `native_text` | 标题、正文、标签、数字、脚注 |
| `native_shape` | 普通卡片、边框、分割线、坐标轴、连接线、胶囊 |
| `transparent_png` | 图标、照片圆章、金属节点、复杂玻璃或光效复合体 |
| `fixed_scene_visual` | 与透视、遮挡或材质强绑定、且用户不要求移动的复杂视觉 |

OCR 只能作为初稿。标题、品牌名、专名、缩写、数字、年份、币种、单位和脚注须在 200%–400% 下对照源图；在 contract 中记录已验证文字与 `AI / Al`、`1 / I / l` 等易混字符检查。

完整的取舍逻辑见 [references/methodology.zh-CN.md](references/methodology.zh-CN.md)，人类可编辑性标准见 [references/human-editability.zh-CN.md](references/human-editability.zh-CN.md)。

## 什么才叫“人类可编辑”

最终页面必须同时满足：

1. **按意义移动：** 卡片、图标、标题条、Logo 单元、圆章、节点和标注是完整操作对象，不能是一堆小图碎片。
2. **规则几何原生化：** 直线、闭合边框、普通圆角矩形、坐标轴和简单箭头应优先使用安全的原生形状。
3. **复杂质感整体保真：** 金属、玻璃、光晕、粒子与 hero visual 可以保留为一个干净的透明复合层。
4. **选择窗格可理解：** 每个重要对象必须有语义名称，例如 `s08_logo_wall_panel`、`s14_milestone_200b`。
5. **重复系统一致：** 重复卡片、圆章、Logo cell、导航组件共享尺寸、边距、圆角规则和 `reuse_key`。
6. **没有微碎片拼图：** 不能用许多小图片重建边线、角、阴影、直线或字母，伪装成“可编辑”。
7. **使用可信画布：** 采用源模板尺寸；无模板时标准 16:9 为 13.333333 × 7.5 in，不能无理由使用双倍画布。

重要对象要记录 `significant: true`、`powerpoint_name`、`movement_unit`，并在适用时提供 `reuse_key`。

## 保真优先的拆分原则

先明确：

- `user_requested_movable`：用户明确要移动、缩放或编辑的对象；
- `preserve_source_pixels`：不需要编辑、且源图已经成功的照片、屏幕、环境 UI 或装饰；
- `hero_visuals`：决定页面质感的平台、飞轮、光路、复杂网络等视觉锚点；
- `script_generated_visuals_forbidden: true`：脚本可以测量、排版和装配，不得粗糙近似高审美视觉。

不得把用户要求移动的对象留在 `clean_base`，也不得为了增加对象数量而破坏获认可的设计。图层边界取决于**人类编辑意图和视觉完整性**，而不是对象数量。

### 必须保留身份的视觉

证据照片、指定建筑、历史图片、产品图片和官方 Logo 必须保留身份：

- 从原始媒体或已验收源页面提取，不能从重生成背景再次裁切；
- 记录视觉锚点和 source-vs-render 证据；
- 官方 Logo 不得生成、描摹、改色或近似。

### 固定场景的边界

若视觉与建筑、人物、表面、透视或遮挡紧密绑定，而用户又不需要移动它，就保留为 `fixed_scene_visual`。其上方文字、普通卡片和明确要求移动的图标仍可拆开。不要把环境像素藏进所谓“透明可移动资产”里。

## 边框、面板、圆章与网格：阻塞性质量门槛

- **边框必须完整：** 金、白或其他闭合镶边持续完整；透明素材四角不能有源底图残片。
- **留出安全边距：** 可见 alpha 边界不能贴素材画布，须为光晕、金边和阴影留空间。
- **圆章必须完整：** 照片圆章、圆环和里程碑节点要闭合、正圆、统一直径，并与容器保留 inset。
- **双框共用接缝：** 标题框与正文框的基线、切角和边框厚度须一致，不能有双线错位或斜线分叉。
- **Logo wall 应分层：** 大底板、标题条、cell 壳体与真实 Logo 相互独立；不得把整面 Logo 墙做成一张不可调节大图。
- **重复模块要量一个母件：** 先测量合格母件再复制定位，不能逐个凭肉眼重画。

如果原生形状无法还原切角、金边、玻璃和发光质感，可以使用“高保真透明壳体 + 原生文字/icon”的混合方案；壳体必须完整、干净、四角透明且有安全边距。

## 图表与高级标注

优先采用混合建模：网格、坐标轴、数据线、虚线、普通引线和文字用原生对象；金属节点、复杂箭头或标注外壳用独立透明资产；文字仍应独立原生可编辑。标注必须准确锚定数据点，逐项核对节点、垂线、箭头和底框的空间关系。

不得用普通圆角矩形代替特殊箭头框，也不得用过大的默认圆角破坏原设计比例。

## 构建与装配

建议每页工作目录：

```text
page_NNN/
|-- clean_base.png
|-- assets/
|-- layer_contract.json
|-- page.pptx
|-- preview.png
|-- clean_base_proof.png
|-- move_away_proof.png
|-- alpha_purity_contact_sheet.png
`-- validation.json
```

构建规则：

- 按语义块建立文本框，不能按视觉行碎片拆字；混色标题用同一文本框中的多个 run；
- 透明 PNG 必须是真实 alpha，无白边、矩形 matte、环境残留或残字；
- 有意识地安排层级，通常为 `clean_base -> fixed/composite visuals -> native shapes -> icons -> text`；
- PowerPoint shape 名与 contract 的 `powerpoint_name` 一致；
- 对每个可移动模块做 move-away 验证，检查对象本身与露出的底图。

独立页面构建或多人并行时，阅读 [references/page-worker-contract.zh-CN.md](references/page-worker-contract.zh-CN.md)。

### 合并策略

- `full_rebuild`：优先通过真实 PowerPoint 的 Slide Sorter 复制已验证页面。
- `local_refinement`：只能补丁 `allowed_change_slides`，并对受保护页面与已验收基线比较。

## QA 关卡

最终交付必须通过：

1. 文字、专名、数字、币种、单位、换行与易混字符准确；
2. 整页和关键 crop 的源图/渲染图对比；
3. 对象类型、语义名称、重复系统、层级和画布尺寸正确；
4. move-away、clean-base-only、透明度与选择窗格检查；
5. OOXML 包检查、contract validation 和 human-editability audit；
6. 真实 Microsoft PowerPoint 打开、保存、关闭、重开和导出时均无 Repair。

```bash
python3 <skill-directory>/scripts/validate_layer_contract.py \
  /absolute/path/layer_contract.json \
  --pptx /absolute/path/page.pptx \
  --report /absolute/path/validation.json

python3 <skill-directory>/scripts/audit_human_editability.py \
  /absolute/path/final.pptx \
  --strict \
  --report /absolute/path/human_editability.json
```

完整质量门槛见 [references/qa-gates.zh-CN.md](references/qa-gates.zh-CN.md)，常见失败与修复见 [references/failure-modes.zh-CN.md](references/failure-modes.zh-CN.md)。仅在源像素无法干净提取时，才使用 [references/imagegen-prompts.zh-CN.md](references/imagegen-prompts.zh-CN.md) 的提示词模式。

## 最终定稿顺序

1. 在真实 Microsoft PowerPoint 中打开、检查、保存、关闭、重开和导出。
2. 仅对可信的本地生成文件，按操作系统需要移除 quarantine。
3. 运行包、contract、编辑性和视觉检查。
4. 记录最终 SHA-256。
5. 计算 SHA 后不能再用可能改写文件的软件打开；若文件改变，必须重新完成 QA 与哈希。

## 如实说明交付边界

- `review_draft` 主要服务快速内容审阅，可能保留扁平视觉；
- BLADE final 必须说明哪些是原生对象、哪些是独立透明资产、哪些为保真留在固定场景；
- 不得把整页图片、切片拼图或文字叠加稿描述为“全分层可编辑”。

交付时提供 PPTX、预览、layer contract、QA 证据、真实 PowerPoint 验证结果、已知保真边界和最终校验和。
