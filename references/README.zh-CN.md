# BLADE Slides 中文参考资料导航

本目录保留英文原始参考资料，便于英文 Agent 直接读取；以下中文文件面向中文用户和审阅者，内容与对应英文文件保持同一方法、边界和质量要求。脚本字段、对象类型和命令参数刻意保留英文，以保证兼容性。

| 中文资料 | 对应英文 | 何时阅读 |
| --- | --- | --- |
| [methodology.zh-CN.md](methodology.zh-CN.md) | [methodology.md](methodology.md) | 设计拆分、确定图层与生产模式时 |
| [human-editability.zh-CN.md](human-editability.zh-CN.md) | [human-editability.md](human-editability.md) | 判断一个 PPT 是否真能像人工制作般编辑时 |
| [page-worker-contract.zh-CN.md](page-worker-contract.zh-CN.md) | [page-worker-contract.md](page-worker-contract.md) | 单页生产、多人协作或合并前交接时 |
| [qa-gates.zh-CN.md](qa-gates.zh-CN.md) | [qa-gates.md](qa-gates.md) | 交付前的视觉、结构和 PowerPoint 验收时 |
| [failure-modes.zh-CN.md](failure-modes.zh-CN.md) | [failure-modes.md](failure-modes.md) | 出现切割残片、错位、Repair 或伪可编辑问题时 |
| [imagegen-prompts.zh-CN.md](imagegen-prompts.zh-CN.md) | [imagegen-prompts.md](imagegen-prompts.md) | 只有在源素材无法干净提取时，才使用图像生成或编辑 |

中文说明不替换 `.json` schema 和 Python 脚本；这些机器可读/可执行接口应保持稳定。若中英文表述出现歧义，以 `SKILL.md` 的结构性字段、脚本行为和验证结果为准，并欢迎提交 issue 修正翻译。
