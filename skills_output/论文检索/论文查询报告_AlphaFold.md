# 论文查询报告

**DOI:** `10.1038/s41586-021-03819-2`
**查询日期:** 2026-06-17
**查询数据库:** Crossref、Semantic Scholar、Unpaywall

---

## 1. 基本信息

| 字段 | 值 |
|---|---|
| **标题** | Highly accurate protein structure prediction with AlphaFold |
| **期刊** | Nature |
| **卷/期/页** | Volume 596, Issue 7873, Pages 583–589 |
| **在线出版** | 2021-07-15 |
| **印刷出版** | 2021-08-26 |
| **出版商** | Springer Science and Business Media LLC |
| **ISSN** | 0028-0836, 1476-4687 |
| **类型** | journal-article |
| **许可证** | CC BY 4.0 (开放获取) |
| **OA 状态** | Hybrid OA |
| **PMID** | 34265844 |
| **PMCID** | PMC8371605 |

---

## 2. 摘要

Proteins are essential to life, and understanding their structure can facilitate a mechanistic understanding of their function. Through an enormous experimental effort, the structures of around 100,000 unique proteins have been determined, but this represents a small fraction of the billions of known protein sequences. Structural coverage is bottlenecked by the months to years of painstaking effort required to determine a single protein structure. Accurate computational approaches are needed to address this gap and to enable large-scale structural bioinformatics. Predicting the three-dimensional structure that a protein will adopt based solely on its amino acid sequence—the structure prediction component of the "protein folding problem"—has been an important open research problem for more than 50 years. Despite recent progress, existing methods fall far short of atomic accuracy, especially when no homologous structure is available. Here we provide the first computational method that can regularly predict protein structures with atomic accuracy even in cases in which no similar structure is known. We validated an entirely redesigned version of our neural network-based model, AlphaFold, in the challenging 14th Critical Assessment of protein Structure Prediction (CASP14), demonstrating accuracy competitive with experimental structures in a majority of cases and greatly outperforming other methods. Underpinning the latest version of AlphaFold is a novel machine learning approach that incorporates physical and biological knowledge about protein structure, leveraging multi-sequence alignments, into the design of the deep learning algorithm.

---

## 3. 作者列表（共 34 位）

| 序号 | 作者 | ORCID |
|------|------|-------|
| 1 | John Jumper (通讯作者) | 0000-0001-6169-6580 |
| 2 | Richard Evans | — |
| 3 | Alexander Pritzel | — |
| 4 | Tim Green | 0000-0002-3227-1505 |
| 5 | Michael Figurnov | — |
| 6 | Olaf Ronneberger | — |
| 7 | Kathryn Tunyasuvunakool | — |
| 8 | Russ Bates | — |
| 9 | Augustin Žídek | — |
| 10 | Anna Potapenko | — |
| 11 | Alex Bridgland | — |
| 12 | Clemens Meyer | — |
| 13 | Simon A. A. Kohl | 0000-0003-4271-4418 |
| 14 | Andrew J. Ballard | — |
| 15 | Andrew Cowie | — |
| 16 | Bernardino Romera-Paredes | — |
| 17 | Stanislav Nikolov | — |
| 18 | Rishub Jain | — |
| 19 | Jonas Adler | 0000-0001-9928-3407 |
| 20 | Trevor Back | — |
| 21 | Stig Petersen | — |
| 22 | David Reiman | — |
| 23 | Ellen Clancy | — |
| 24 | Michal Zielinski | — |
| 25 | Martin Steinegger | 0000-0001-8781-9753 |
| 26 | Michalina Pacholska | 0000-0002-2160-6226 |
| 27 | Tamas Berghammer | — |
| 28 | Sebastian Bodenstein | — |
| 29 | David Silver | 0000-0002-5197-2892 |
| 30 | Oriol Vinyals | — |
| 31 | Andrew W. Senior | 0000-0002-2401-5691 |
| 32 | Koray Kavukcuoglu | — |
| 33 | Pushmeet Kohli | — |
| 34 | Demis Hassabis | 0000-0003-2812-9917 |

> **通讯作者:** John Jumper (jumper@deepmind.com) 与 Demis Hassabis (dhcontact@deepmind.com)
>
> **所属机构:** 除 Martin Steinegger（首尔大学）外，其余作者均来自 DeepMind, London, UK。

---

## 4. 引用指标

| 指标 | 数值 | 来源 |
|------|------|------|
| **被引次数** | 36,510 | Semantic Scholar |
| **有影响力引用** | 3,746 | Semantic Scholar |
| **Crossref 被引次数** | 41,993 | Crossref |
| **参考文献数** | 84 (Crossref) / 93 (Semantic Scholar) | — |

---

## 5. 开放获取信息

| 字段 | 值 |
|------|-----|
| **是否 OA** | ✅ 是 |
| **OA 类型** | Hybrid（混合开放获取） |
| **许可证** | CC BY 4.0 |
| **出版商 PDF** | https://www.nature.com/articles/s41586-021-03819-2.pdf |
| **PMC 全文** | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8371605 |
| **DOI 页面** | https://doi.org/10.1038/s41586-021-03819-2 |

---

## 6. Semantic Scholar TLDR

> This work validated an entirely redesigned version of the neural network-based model, AlphaFold, in the challenging 14th Critical Assessment of protein Structure Prediction (CASP14), demonstrating accuracy competitive with experimental structures in a majority of cases and greatly outperforming other methods.

---

## 7. 数据库查询状态

| 数据库 | 状态 | 端点 |
|--------|------|------|
| **Crossref** | ✅ 成功 | `GET /works/10.1038/s41586-021-03819-2` |
| **Semantic Scholar** | ✅ 成功 | `GET /graph/v1/paper/DOI:10.1038/s41586-021-03819-2` |
| **Unpaywall** | ✅ 成功 | `GET /v2/10.1038/s41586-021-03819-2` |

---

## 8. 论文概要

这是 DeepMind 团队于 2021 年发表在 **Nature** 上的 AlphaFold 论文。该工作提出了首个能够在**即使没有同源结构的情况下，仍以原子级精度**预测蛋白质三维结构的方法。在 CASP14 评估中，AlphaFold 展现出与实验结构相媲美的精度，大幅超越其他方法。这是一项蛋白质结构预测领域的里程碑式工作，迄今已被引用超过 36,000 次。论文为开放获取（CC BY 4.0），可通过上述链接免费获取 PDF。