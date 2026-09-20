# 页面工作单元契约

本文件定义一张重建页面进入合并前的最低证据要求；单 Agent 或多页面工作单元都采用相同结构。

## 输入

- 已验收的整页源图；
- 精确页面尺寸（像素和英寸）；
- 含生产模式的 layer contract；
- 已验证文字清单、字体和换行锁定；
- 真实 Logo 与身份关键媒体；
- 已验收系统量测或 `reuse_key` 来源；
- 局部优化时的 baseline PPTX、允许修改页和受保护页。

## 必须输出

```text
page_NNN/
├── clean_base.png
├── assets/
├── layer_contract.json
├── page.pptx
├── preview.png
├── clean_base_proof.png
├── move_away_proof.png
├── alpha_purity_contact_sheet.png
├── source_vs_render.png
├── key_crops/
└── validation.json
```

## 职责

1. 不得编造文案、Logo、数据、人物、产品或品牌元素。
2. 不得修改其他页面目录或共享基线。
3. 每个重要资产和 PowerPoint shape 必须语义化命名。
4. 规则几何使用原生形状；光学材质采用保真复合素材。
5. 不得用微小栅格切片伪造边框、角、直线或字母。
6. 验证完整边缘、圆形、重复网格量测和有意义移动单位。
7. 保存真实 move-away 证据，不能只有“可移动”的文字声明。
8. 报告每个固定视觉及其必须固定的理由。

## 验证与合并交接

只有当 contract validator、源图/渲染图对比、重要对象名、底图与前景互斥、PowerPoint 无 Repair 打开，以及 `validation.json` 无 blocker 都通过后，页面才能进入合并。

`full_rebuild` 只交付一张已验证页面，父级组装器通过 Microsoft PowerPoint 按顺序复制；`local_refinement` 交付改动页与受保护页面比较报告，不能替换或重生成未触及页面。
