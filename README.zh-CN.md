# 面向力学研究的五套 Codex Skills

这套包把研究想法、文献 gap、论文叙事和 FEM 验证串起来，每套都可以单独安装。入口采用官方的 `SKILL.md` + YAML 格式，同时附上可执行脚本、工作模板、领域说明和正反例测试。

**Skill 的入口本来就是文字指令。** 有用与否取决于它是否提供了具体的工作方法、工具和判定依据。脚本不是每个 Skill 的必选项；这里加入脚本，是因为证据追踪、边界区域检查和数值后处理确实值得重复使用。

## 从实际研究工作中提炼的经验

| 可复用经验 | 为什么有价值 | 本包怎样实现 |
|---|---|---|
| 先确认解析与 FEM 是同一个物理问题 | 曲线接近可能来自不同边界、方向或归一化 | FEM registration 与适配器约定 |
| 分清校准、留出预测与机制解释 | 重新拟合后吻合不能证明盲预测能力 | significance 输入审计检查组别泄漏 |
| 分开 release、fold、force drop、有限跳跃和落点 | 这些事件对应不同数学与物理证据 | stability 参考、能量审核、事件候选提取 |
| 从“这个变化影响什么决定”解释意义 | 几何或图案改变不自动构成科学贡献 | decision → mechanism → falsifier 模板 |
| Main／SI 改写时保留最强证据与失败案例 | 新版本更简洁也可能丢失关键论证 | required_assets 与证据 hash 审计 |
| 先做最小决定性验证 | 避免在错误分支上继续增加分析和图 | 竞争解释、控制组、最便宜的区分性实验 |

这里只公开抽象经验、原创辅助脚本和合成示例，没有上传原始聊天、未发表论文或实际试件资料。

## 五套 Skill 的具体用途

### 1. research-significance：为什么值得做

输入研究问题、基线、物理机制和现有证据，产出一段意义陈述、一张贡献—证据—边界表，以及能推翻核心假设的测量标准。不会用“novel / programmable”替代机制解释，也不会给意义打一个看起来精确的总分。

脚本检查问题是否完整、竞争解释是否有区分性测试、证据角色是否支持所声明层级、校准与留出样本是否重叠。真正的科学价值仍需要读源材料判断。

### 2. research-gap：别人解决到哪里，你还缺什么

输入研究方向和文献，搜索并打开原始论文，产出最近工作能力矩阵和有范围的 gap 候选。包含检索日志 CSV、DOI 去重和引用依据检查。无法获取全文要标记 unknown；有限检索不能证明“从来没人做过”。

### 3. research-writing：把研究写清楚，同时保住证据

从完整 Main／SI 和证据清单出发，先冻结需要保留的结论、核心图、控制组和失败案例，再改写。用 claim ID、figure ID 和文件 hash 查遗漏或证据变化。主文讲清物理问题与机制，SI 留下可复现细节。脚本检查追踪和保存关系，语言与科学含义由 Codex 阅读判断。

### 4. fem-explicit-bifurcation：可适配的验证模块

提供命名边界区域、DOF 冲突检查、Abaqus INP 生成、真实 ODB 读取、动能／内能窗口检查、force-drop／持续 opening 候选提取，以及解析 fold／pitchfork 基准。模板可运行，但它的物理模型是直梁弹性 B21 悬臂。

通用部分是注册、选择检查、执行证据、后处理和结论分级。接触、周期约束、复杂材料、真实分支切换、受约束特征模态需要针对项目写 adapter。Explicit 的动态轨迹不能直接叫静态平衡分支，解析 normal form 测试不能冒充 FEM 分岔验证。

### 5. research-word：把推导、后处理和图写成完整 Word

围绕每节的物理问题整理样本、控制变量、输入、推导、后处理、图板和结论，再生成或修改用户指定的 Word。保留完整能量的交叉项，说明任何约束代入或凝聚的依据。使用可用文档工具生成可编辑公式、图注和引用，优先沿用用户的模板。

附带标准库 DOCX 检查器与三个合成测试，可发现缺失的嵌入图和统计公式、标题、图注。版面仍要渲染后检查；渲染接口失效时保留已有 Word，采用已授权的可用后备方式，或明确交付为尚未完成版面检查的工作稿，不反复索取相同许可。详见 [Research Word](docs/RESEARCH_WORD.md)。

## 安装

在终端执行：

```powershell
git clone https://github.com/DJDeborah/research-mechanics-skills.git
cd research-mechanics-skills
python tools/install.py --user
```

新开一个 Codex 任务／下一轮对话后，用 `$research-significance`、`$research-gap`、`$research-writing`、`$research-word` 或 `$fem-explicit-bifurcation` 调用。也可以在 Codex 中直接使用内置 `$skill-installer` 安装本仓库的五个 `skills/<name>` 路径。详见 [安装指南](docs/INSTALL.md)。

只让某个项目使用时：

```powershell
python tools/install.py --project 'D:\my-research-project'
```

安装器会复制完整目录到项目 `.agents/skills/`，遇到同名目录会停止，不覆盖旧版。

## 五个直接可用的调用示例

```text
$research-significance
基于这个研究目录，说明改变边界条件到底改变了什么科学或设计决定。
给出竞争机制、可测量的反例条件与最便宜的区分性测试。
已有吻合分开标明 calibration 和 holdout；没有证据就保持 proposed。
```

```text
$research-gap
为我的 buckling metamaterial 研究查找最近的原始论文。
比较平衡分支、接触释放、动态落点、跨边界条件迁移这几种能力。
保存检索日志和具体段落定位，主动寻找推翻 gap 的论文；不要写 first-ever。
```

```text
$research-writing
结合完整 Main、SI、图和证据清单重写这个 Results 小节。
先列需要保留的结论、图和失败案例，再输出英文新稿与 change log。
写清物理意义和变量定义，区分拟合、预测、失稳与实际跳跃。
```

```text
$fem-explicit-bifurcation
先运行包里的 beam smoke 示例，核对 ROOT／TIP 实际节点、DOF 和单位。
使用 double=both 跑 Abaqus Explicit 并读取 ODB，检查能量与反力。
然后为我的真实模型列出需要替换的 adapter 项，分别说明动态事件与分岔还缺哪些证据。
```

```text
$research-word
结合我指定的 Word、当前计算与以前的完整结果，按物理问题重写分析。
每节对应样本、变量、推导、后处理、数据图与结论，保留最强证据。
输出实际 DOCX，公式尽量可编辑；沿用模板，渲染失败则说明工作稿状态。
```

## 验证是否好用

先运行无许可证验证：

```powershell
python -m unittest discover -s tests -v
python tools/run_demo.py --out local-runs/demo
```

再运行实际 Explicit 验证（需要已安装并有许可证的 Abaqus）：

```powershell
python tools/run_abaqus_smoke.py --abaqus 'D:\path\to\abaqus.bat' --out local-runs/explicit --sensitivity
```

已测结果和限制在 [验证报告](docs/VALIDATION_REPORT.md)。安装后如何检查 Codex 真正触发 Skill、如何做无 Skill／有 Skill 对照，以及如何用新的研究样本验证迁移能力，在 [Codex 使用验证指南](docs/CODEX_VALIDATION.md)。已有脚本测试不等于证明模型写作质量或科研能力提升。

## 开源来源与发布

参考了 K-Dense 的 hypothesis-generation／scientific-writing、FEMIS 的 V&V、CAE-Agent-Hub 的 Abaqus 工作流和 UCL-ERL 的论文—代码一致性审计。没有把它们的全部流程和无关要求塞进来；新代码以 MIT 发布。具体固定 commit、来源许可证和已测范围见 [来源说明](docs/SOURCES.md)。

仓库可以克隆、下载 ZIP、单独安装 Skill；同时附有 `plugin.json`。GitHub 发布与 OpenAI 公共插件目录上架是两件事，本包没有声明完成后者。
