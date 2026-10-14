# Changelog｜更新记录

## V2.2.0 — 2026-10-14

### Added｜新增

- Bounded multi-agent orchestration for multi-page decks: freeze a reviewed pilot, delegate isolated page groups, and keep integration plus whole-deck QA with one parent task / 新增多页 deck 的有界多 Agent 编排：先冻结已审核试点页，再隔离委派页面组，由单一父级负责集成与整 deck QA。
- Guidance for choosing sub-agents versus separate sessions, preventing overlapping writes, and falling back to sequential work when coordination is not safe or worthwhile / 明确 sub-agent 与独立 session 的选择、并发写入隔离及不适合并行时的顺序执行策略。

### Changed｜调整

- New contracts use skill version 2.2.0; validator continues accepting contracts from 2.0.0 through 2.1.1 / 新 contract 使用 skill_version 2.2.0；验证器继续兼容 2.0.0–2.1.1 版本的 contract。

## V2.1.1 — 2026-09-22

### Fixed｜修正

- Material-aware decomposition precedes ordinary geometry / 先判断复杂材质，再判断普通几何。
- Validate glass opacity in the actual layered composition; pilot one representative panel before repeating / 在实际叠层中验证玻璃透明度，先检查代表性面板再复制同类系统。
- Protect non-target objects on the edited slide and restrict changes to named properties / 局部修改精确到对象与属性，同页未点名对象也受保护。
- Updated English and Chinese guidance together. No script, schema or CLI changes; no measured token-saving claim / 中英文同步；脚本、schema 和命令行不变，不宣称已验证 Token 节省。

## V2.1.0 — 2026-09-20

### Added｜新增

- Chinese-first bilingual GitHub landing page / 中文优先的中英双语 GitHub 首页。
- Complete Chinese skill instructions in `SKILL.zh-CN.md` / 完整中文 Skill 说明。
- Chinese companion guides for methodology, human editability, page handoff, QA, failure recovery, and ImageGen prompting / 方法、编辑性、页面交接、QA、失败修复与 ImageGen 提示词的中文资料。
- Bilingual display name, description, and default prompt in `agents/openai.yaml` / 双语界面元数据。

### Changed｜调整

- Added cross-links between the English and Chinese documentation while retaining stable script names, schema fields, and command-line interfaces / 在中英文资料间加入互链，同时保持脚本名称、schema 字段与命令行接口稳定。

## V2.0.0 — 2026-09-20

- First public-safe release / 首个可公开分享版本。
