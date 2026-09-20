# ImageGen 提示词模式

只在源像素无法通过提取干净保留时使用。始终附上已验收源图，并明确哪些内容必须不变。生成后必须检查黑/白/棋盘格、完整边缘和 move-away；改变身份或几何的输出应拒绝。

## 干净底图

```text
Edit the supplied 16:9 slide image into a clean scene plate.
Remove only: [EXACT MOVABLE OBJECTS].
Preserve exactly: composition, camera, architecture, lighting, palette, landscape,
approved fixed hero visual, and all source-critical imagery.
Naturally reconstruct only the areas exposed by the removed objects.
Do not add text, logos, panels, icons, borders, or generic UI.
Output one 3840x2160 clean background image.
```

中文意图：只移除精确列出的可移动对象，其他构图、镜头、建筑、灯光、色调、固定 hero 与身份关键视觉必须保持；只自然补全露出的环境，不能新增文字、Logo、面板、icon、边框或通用 UI。

## 透明面板壳体

```text
Recreate only the referenced panel shell as a separate transparent PNG.
Preserve its exact proportions, complete continuous border, cut-corner geometry,
gold/white edge treatment, glass material, highlight and restrained shadow.
Remove all text, icons, logos and environmental background pixels.
Leave generous transparent safety padding around every visible edge and glow.
The four corners of the PNG canvas must be fully transparent.
```

中文意图：只重建面板外壳，保持比例、闭合边框、切角、金/白边、玻璃材质和克制阴影；移除文字、icon、Logo 和环境像素；可见边缘/光晕外留足透明安全边距，四角完全透明。

## 完整圆形圆章

```text
Reconstruct the referenced circular photo medallion as one transparent PNG.
The entire circle and every ring must be visible and geometrically round.
Preserve the source photo identity, camera direction, gold/white trim and subtle shadow.
Do not crop the left, right, top or bottom rim. Add transparent safety padding.
Do not include any card background or adjacent text.
```

中文意图：整个圆和每一层圆环必须完整可见、几何正圆；保留照片身份、镜头方向、金/白镶边和细微阴影；不能裁掉任何边缘；不带卡片背景或邻近文字。

## 金属里程碑节点或箭头壳体

```text
Recreate only the referenced metallic milestone node / shaped arrow shell.
Preserve the source silhouette, gold material, highlight, glow and transparency.
Remove every word and number so native PowerPoint text can be placed above it.
Do not simplify it into a generic rounded rectangle or flat circle.
Output a clean transparent PNG with safety padding and no environmental pixels.
```

中文意图：只重建金属节点或特殊箭头外壳，保留轮廓、金属质感、高光、光晕和透明度；移除所有文字和数字，供 PPT 原生文字单独放置；不能简化成普通圆角矩形或扁平圆。

## 身份关键对象清理

```text
Use the supplied source crop as identity truth.
Remove only the overlaying label, border or obstruction: [ITEM].
Do not change the subject, logo, camera, orientation, landmark, color or proportions.
Return the complete object with transparent background and natural missing-detail repair.
```

中文意图：以源裁切作为身份真相，只移除指定遮挡；不得改变主体、Logo、镜头、方向、地标、颜色或比例；返回完整透明对象并自然修补被遮挡细节。
