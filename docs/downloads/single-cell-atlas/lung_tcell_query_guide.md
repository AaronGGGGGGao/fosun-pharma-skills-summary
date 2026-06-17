# 肺组织T细胞单细胞转录组数据查询指南

## 查询需求概述

**物种**: Homo sapiens (人类)  
**组织**: Lung / Lung tissue (肺组织)  
**疾病状态**: Normal (正常) 和 COVID-19  
**细胞类型**: T细胞亚群，包括:
- CD4-positive T cell (CD4+ T细胞)
- CD8-positive T cell (CD8+ T细胞)  
- Regulatory T cell (调节性T细胞)
- Exhausted T cell (耗竭T细胞)
- Memory T cell (记忆T细胞)
- 其他T细胞亚群

**数据类型**: Single-cell RNA-seq (单细胞RNA测序)

---

## 数据源

**CZ CELLxGENE Census** - 全球最大的单细胞转录组公共数据库之一
- 当前稳定版本: 2025-11-08
- 总细胞数: 217+ million (2.17亿+)
- 包含人类、小鼠等多个物种
- 标准化的细胞类型、组织、疾病注释

---

## 查询方法

### 方法1: 使用 CELLxGENE Census API (推荐)

#### 安装依赖

```bash
pip install "cellxgene-census==1.17.*"
pandas
scanpy
```

#### 查询代码

```python
import cellxgene_census
import pandas as pd
import json

# 打开Census数据库
with cellxgene_census.open_soma() as census:
    
    # 定义T细胞类型
    tcell_types = [
        'T cell',
        'CD4-positive, alpha-beta T cell',
        'CD8-positive, alpha-beta T cell',
        'regulatory T cell',
        'exhausted T cell',
        'effector memory CD8-positive, alpha-beta T cell',
        'effector memory CD4-positive, alpha-beta T cell',
        'central memory CD8-positive, alpha-beta T cell',
        'central memory CD4-positive, alpha-beta T cell',
        'T-helper 1 cell',
        'T-helper 17 cell',
        'T-helper 2 cell',
        'cytotoxic T cell',
        'CD4-positive helper T cell',
        'gamma-delta T cell'
    ]
    
    # 构建查询过滤条件
    cell_type_filter = ", ".join([f"'{ct}'" for ct in tcell_types])
    obs_value_filter = f"""
        tissue_general == 'lung' and 
        is_primary_data == True and
        cell_type in [{cell_type_filter}]
    """
    
    # 查询细胞元数据
    print("正在查询肺组织T细胞数据...")
    cell_metadata = cellxgene_census.get_obs(
        census,
        "homo_sapiens",
        value_filter=obs_value_filter,
        column_names=[
            "cell_type",
            "tissue",
            "tissue_general",
            "disease",
            "disease_ontology_term_id",
            "assay",
            "sex",
            "donor_id",
            "dataset_id",
            "development_stage",
            "self_reported_ethnicity"
        ]
    )
    
    print(f"\n找到 {len(cell_metadata):,} 个T细胞")
    
    # 统计疾病分布
    print("\n【疾病状态分布】")
    disease_counts = cell_metadata['disease'].value_counts()
    for disease, count in disease_counts.items():
        pct = count / len(cell_metadata) * 100
        print(f"  {disease}: {count:,} ({pct:.1f}%)")
    
    # 统计细胞类型分布
    print("\n【T细胞亚群分布】")
    cell_type_counts = cell_metadata['cell_type'].value_counts()
    for ct, count in cell_type_counts.items():
        pct = count / len(cell_metadata) * 100
        print(f"  {ct}: {count:,} ({pct:.1f}%)")
    
    # Normal vs COVID-19对比分析
    print("\n【Normal vs COVID-19 对比】")
    normal_cells = cell_metadata[cell_metadata['disease'] == 'normal']
    covid_cells = cell_metadata[cell_metadata['disease'] == 'COVID-19']
    
    print(f"  Normal样本: {len(normal_cells):,} 个T细胞")
    print(f"  COVID-19样本: {len(covid_cells):,} 个T细胞")
    
    if len(normal_cells) > 0 and len(covid_cells) > 0:
        print("\n  主要T细胞亚群对比:")
        for ct in ['CD4-positive, alpha-beta T cell', 
                   'CD8-positive, alpha-beta T cell',
                   'regulatory T cell',
                   'exhausted T cell']:
            n_count = len(normal_cells[normal_cells['cell_type'] == ct])
            c_count = len(covid_cells[covid_cells['cell_type'] == ct])
            n_pct = n_count / len(normal_cells) * 100
            c_pct = c_count / len(covid_cells) * 100
            print(f"\n    {ct}:")
            print(f"      Normal: {n_count:,} ({n_pct:.1f}%)")
            print(f"      COVID-19: {c_count:,} ({c_pct:.1f}%)")
    
    # 获取相关数据集信息
    print("\n【相关数据集】")
    dataset_ids = cell_metadata['dataset_id'].unique()
    print(f"  涉及 {len(dataset_ids)} 个数据集")
    
    datasets = census["census_info"]["datasets"].read().concat().to_pandas()
    relevant_datasets = datasets[datasets['dataset_id'].isin(dataset_ids)]
    
    for idx, row in relevant_datasets.iterrows():
        print(f"\n  数据集: {row['title']}")
        print(f"  ID: {row['dataset_id']}")
        print(f"  疾病: {row['disease']}")
        print(f"  细胞数: {row['cell_count']:,}")
        print(f"  组织: {row['tissue']}")
    
    # 保存结果
    results = {
        "total_t_cells": len(cell_metadata),
        "disease_distribution": disease_counts.to_dict(),
        "cell_type_distribution": cell_type_counts.to_dict(),
        "normal_count": len(normal_cells),
        "covid_count": len(covid_cells),
        "dataset_count": len(dataset_ids),
        "datasets": relevant_datasets.to_dict('records')
    }
    
    with open('tcell_query_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # 保存细胞元数据
    cell_metadata.to_csv('tcell_metadata.csv', index=False, encoding='utf-8-sig')
    
    print("\n查询完成！结果已保存。")
```

---

### 方法2: 使用 CELLxGENE Discover 网站

访问: https://cellxgene.cziscience.com/

1. 在搜索框输入: `lung` 或 `T cell`
2. 使用筛选器:
   - **Organism**: Homo sapiens
   - **Tissue**: lung, lung parenchyma, lung tissue
   - **Disease**: normal, COVID-19
   - **Cell type**: T cell, CD4-positive T cell, CD8-positive T cell, etc.
   - **Assay**: 10x 3' v3, 10x 5' v1, etc.

3. 下载感兴趣的数据集 (H5AD格式)

---

## 预期结果示例

### 数据结构

查询结果将包含以下信息:

```
总细胞数: ~50,000-200,000 个T细胞
涉及数据集: 10-30 个研究
供体数: 50-200 个个体
疾病状态:
  - normal: ~30-50%
  - COVID-19: ~20-40%
  - 其他疾病: ~20-30%
```

### T细胞亚群分布 (示例)

```
CD4-positive, alpha-beta T cell: 35%
CD8-positive, alpha-beta T cell: 30%
regulatory T cell: 5%
exhausted T cell: 3%
memory T cells: 15%
其他T细胞: 12%
```

### Normal vs COVID-19 对比 (示例)

```
CD4+ T细胞:
  Normal: 40% (12,000 cells)
  COVID-19: 30% (8,000 cells)

CD8+ T细胞:
  Normal: 25% (7,500 cells)
  COVID-19: 35% (9,500 cells)

Regulatory T细胞:
  Normal: 5% (1,500 cells)
  COVID-19: 8% (2,200 cells)

Exhausted T细胞:
  Normal: 2% (600 cells)
  COVID-19: 5% (1,350 cells)
```

---

## 下游分析建议

获取数据后，可进行以下分析:

1. **差异表达分析**
   - 比较COVID-19 vs Normal中各T细胞亚群的基因表达差异
   - 关注免疫相关基因: IFNG, TNF, IL2, IL10, PDCD1 (PD-1), CTLA4, etc.

2. **细胞状态分析**
   - T细胞耗竭标志物: PDCD1, LAG3, TIGIT, HAVCR2 (TIM-3), TOX
   - 效应功能标志物: GZMB, PRF1, IFNG, TNF
   - 调节性标志物: FOXP3, IL2RA (CD25), CTLA4

3. **轨迹推断分析**
   - T细胞分化轨迹
   - 从naive到effector/memory/exhausted的转变

4. **细胞通讯分析**
   - T细胞与其他免疫细胞的相互作用
   - 配体-受体对分析

---

## 参考资源

- **CELLxGENE Census 文档**: https://chanzuckerberg.github.io/cellxgene-census/
- **CELLxGENE Discover**: https://cellxgene.cziscience.com/
- **相关研究**: 
  - Liao et al. (2020) - Single-cell landscape of immunological responses in mild and severe COVID-19
  - Su et al. (2020) - Single-cell multi-omics analysis of SARS-CoV-2 infection

---

## 注意事项

1. **数据规模**: 肺组织T细胞数据量较大，建议在有足够内存的环境中运行 (推荐 16GB+ RAM)
2. **查询时间**: 大型查询可能需要 5-15 分钟
3. **数据质量**: 只使用 `is_primary_data == True` 的细胞以避免重复计数
4. **版本控制**: 使用固定的 Census 版本 (如 `census_version="2025-11-08"`) 以保证可重复性

---

**生成时间**: 2026-06-17  
**数据来源**: CZ CELLxGENE Census  
**分析工具**: cellxgene-census Python API
