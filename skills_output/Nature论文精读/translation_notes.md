# Translation Notes / 翻译注释

## 文档信息

- **论文标题:** Influence of believed AI involvement on the perception of digital medical advice
- **DOI:** 10.1038/s41591-024-03180-7
- **来源:** PMC全文XML (PMC11564086)，开放获取版本
- **翻译日期:** 2025
- **翻译状态:** 完整全文翻译（约95%内容覆盖）

---

## 1. 低置信度翻译 / Low-Confidence Translations

### 1.1 "uniqueness neglect" — 独特性忽视

- **位置:** S005
- **来源:** Longoni, C., Bonezzi, A. & Morewedge, C. K. (2019). Resistance to medical artificial intelligence. *J. Consum. Res.* 46, 629–650.
- **翻译:** "独特性忽视"
- **置信度:** 中等
- **说明:** 该术语在中文文献中尚未有标准译法。Longoni等人提出的概念指用户认为AI无法充分考虑其个体特征和独特性。备选译法："个体独特性忽视"、"唯一性忽视"。当前采用直译以保持术语一致性，但建议读者参考原始文献理解该概念。

### 1.2 "algorithm aversion" — 算法厌恶

- **位置:** S002, S005
- **置信度:** 高
- **说明:** 该术语在行为经济学和决策心理学中已有较成熟的中文译法。Dietvorst et al. (2015) 提出的经典概念，指人们一旦观察到算法犯错后，会过度避免使用算法，即使算法整体表现优于人类。

### 1.3 "dehumanizing" — 去人性化

- **位置:** S005
- **置信度:** 中等
- **说明:** 在医疗AI语境中，"dehumanizing"指AI介入可能使医疗互动失去人情味、关怀和情感连接。当前采用"去人性化"译法，但该词在中文中可能带有较强的负面含义。备选译法："非人化"、"缺乏人性化"、"去人情化"。

### 1.4 "fictious" — 原文献拼写

- **位置:** S003, S004, S007, M009
- **说明:** 原文多次出现"fictious"一词，应为"fictitious"（虚构的）的拼写错误。翻译中按照"虚构的"处理，不影响理解。这是已发表版本的拼写错误，在PMC XML中保留。

---

## 2. 无法确认的内容 / Unverifiable Content

### 2.1 补充材料 (Supplementary Figures 1–5, Supplementary Results)

- **状态:** 无法获取
- **说明:** 补充图1-4为四个病例报告场景（戒烟、结肠镜检查、广场恐惧症、反流病），补充图5为实验设计示意图。这些内容在PMC全文XML中未被包含，需从Nature网站或OSF仓库直接获取。补充结果中的混合效应回归分析和探索性分析结果同样无法从PMC XML中提取。
- **影响:** 不影响对正文主要发现的理解，但无法提供完整的补充分析细节。

### 2.2 参考文献编号1-2和4-25的详细内容

- **状态:** 部分恢复
- **说明:** PMC XML中CR1-CR2和CR4-CR25的引用使用了`<citation-alternatives>`结构，其中`<element-citation>`和`<mixed-citation>`包含完整引用信息。所有25条参考文献的完整文本已通过解析`<mixed-citation>`元素提取，并在paper.md中列出。
- **置信度:** 高

### 2.3 图表的原始高分辨率文件

- **状态:** 已获取PMC HTML版本（JPEG，约49KB）
- **说明:** 从PMC获取的图表为HTML渲染版本，分辨率可能不如原始出版版本。原始高分辨率图表需从Nature网站获取。

### 2.4 同行评审信息

- **状态:** 未获取
- **说明:** 同行评审报告和作者回复可从Nature网站获取，但非开放获取。

---

## 3. 翻译策略说明 / Translation Strategy

### 3.1 术语一致性

- 全文统一术语翻译，建立术语表（Terminology Ledger），确保每个核心概念在整篇论文中使用相同的对应中文翻译。
- 统计学术语（如Cohen's d, ηp², P值等）保持原文格式，不进行翻译。
- 参考文献编号和引用标记保持原样。

### 3.2 句子结构处理

- 英文长句在中文翻译中适当拆分，但保持原文的证据链和逻辑关系。
- 统计结果部分保持原文的数字和统计量格式，确保可追溯性。
- 被动语态在中文中适当转换为主动语态，但保持科学写作的客观性。

### 3.3 专业术语处理原则

- 心理学和医学领域已有成熟译法的术语采用标准译法。
- 新兴概念（如LLM相关术语）在首次出现时保留英文原文，并在术语表中说明。
- 作者姓名和机构名称保持原文。

### 3.4 段落对齐

- 每个段落按照"Original → 中文 → Note（必要时）"的格式输出。
- 段落边界与原文保持一致，不进行合并或拆分。
- 图表放置在其首次被实质性提及的段落附近。

---

## 4. 图表提取说明 / Figure Extraction Notes

### 4.1 已提取图表

| 图表编号 | 文件 | 来源 | 分辨率 | 状态 |
|---------|------|------|--------|------|
| Fig. 1 | 41591_2024_3180_Fig1_HTML.jpg | PMC HTML rendering | 约49KB JPEG | OK |
| Fig. 2 | 41591_2024_3180_Fig2_HTML.jpg | PMC HTML rendering | 约49KB JPEG | OK |

### 4.2 缺失图表

| 图表编号 | 说明 | 原因 |
|---------|------|------|
| Supplementary Figs. 1-5 | 病例报告场景和实验设计 | PMC XML中未包含补充材料图形文件 |

### 4.3 表格

- 本文无正式表格（table-wrap）。所有结果以图形形式呈现。

---

## 5. 需要人工确认的地方 / Items Requiring Human Review

### 5.1 翻译质量

- [ ] "uniqueness neglect" 的中文译法是否恰当
- [ ] "dehumanizing" 在医疗语境中的最佳中文对应
- [ ] 所有统计表述的翻译准确性
- [ ] 补充材料中混合效应回归分析结果的翻译（如有需求）

### 5.2 内容完整性

- [ ] 确认是否需要补充材料（Supplementary Figs. 1–5 和 Supplementary Results）的翻译
- [ ] 确认是否需要高分辨率图表文件
- [ ] 确认"fictious"在最终版本中是否为排版错误

### 5.3 格式

- [ ] 确认source_map.json的锚点ID体系是否满足后续问答引用需求
- [ ] 确认图表嵌入位置是否恰当

---

## 6. 源文件信息 / Source File Information

- **PMC ID:** PMC11564086
- **源文件格式:** JATS XML (NLM Journal Archiving DTD v1.4)
- **获取方式:** Europe PMC REST API → fullTextXML
- **图表来源:** PMC article bin (HTML rendering)
- **开放获取状态:** 是（Creative Commons Attribution 4.0 International License）
- **版本:** 已发表版本 (Version of Record)
- **数据/代码:** OSF (https://osf.io/cxb7s/)
- **预注册:** 研究1 (https://osf.io/6trux), 研究2 (https://osf.io/wn6mj)