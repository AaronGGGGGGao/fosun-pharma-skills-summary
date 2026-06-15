```mermaid
flowchart TD
    A[Advanced/Metastatic NSCLC<br/>First-Line Treatment Decision] --> B{EGFR Mutation Status}
    
    B -->|Exon 19 Del or L858R| C{ECOG PS and<br/>CNS Status}
    B -->|Wild-type or other| D[Other Treatment Pathways<br/>See NCCN Guidelines]
    
    C -->|ECOG 0-1<br/>No CNS Mets| E[Standard Risk<br/>Osimertinib 80mg QD<br/>GRADE 1A<br/>PFS 18.9mo, OS 38.6mo]
    
    C -->|ECOG 0-1<br/>CNS Mets or High Burden| F{High-Risk Features}
    C -->|ECOG 2| G[Consider Osimertinib<br/>with close monitoring<br/>or Best Supportive Care]
    
    F -->|TP53 co-mutation<br/>Multiple brain mets<br/>High tumor burden| H[Combination Therapy<br/>Osimertinib + Chemo<br/>GRADE 1B<br/>PFS 25.5mo]
    
    F -->|Amivantamab available<br/>IV therapy acceptable| I[Amivantamab + Lazertinib<br/>GRADE 1B<br/>PFS 23.7mo]
    
    F -->|Standard approach preferred| E
    
    E --> J[Monitoring Plan<br/>Imaging: Every 8-12 weeks<br/>CNS MRI: Baseline + PRN<br/>Labs: CBC, CMP, LFTs q3mo<br/>ECG, LVEF: Baseline + PRN]
    
    H --> J
    I --> J
    G --> J
    
    J --> K{Disease Progression}
    K -->|Yes| L[Re-biopsy Assessment<br/>Tissue + Liquid Biopsy<br/>Resistance Mechanism Analysis]
    K -->|No| J
    
    L --> M[Second-Line Options<br/>Platinum-pemetrexed<br/>Amivantamab + chemo<br/>Clinical trials<br/>Targeted therapy if actionable]
    
    style E fill:#90EE90,stroke:#2E7D32,stroke-width:3px
    style H fill:#FFD54F,stroke:#F57C00,stroke-width:2px
    style I fill:#FFD54F,stroke:#F57C00,stroke-width:2px
    style G fill:#81D4FA,stroke:#1565C0,stroke-width:2px
    style M fill:#FFAB91,stroke:#D84315,stroke-width:2px
```

**Clinical Decision Algorithm: EGFR Exon 19 Deletion NSCLC First-Line Treatment**

**Entry Criteria:**
- Diagnosis: Advanced/metastatic NSCLC (Stage IIIB/IV)
- Biomarker: EGFR exon 19 deletion confirmed (NGS or PCR)
- Setting: First-line, no prior systemic therapy
- Patient: ECOG PS 1, no confirmed brain metastases, adequate organ function

**Key Decision Points:**

1. **EGFR Mutation Confirmation** - Mandatory before treatment initiation
   - Exon 19 deletion or L858R → EGFR TKI pathway
   - Exon 20 insertion → Different pathway (amivantamab, mobocertinib)

2. **Performance Status & CNS Assessment**
   - ECOG 0-1 without CNS mets → Standard osimertinib monotherapy (preferred)
   - ECOG 0-1 with CNS mets or high burden → Consider combination therapy
   - ECOG 2 → Osimertinib with caution or best supportive care

3. **High-Risk Feature Evaluation** (for combination consideration)
   - TP53 co-mutation
   - Multiple brain metastases
   - High tumor burden
   - Aggressive disease kinetics

4. **Treatment Selection**
   - **Osimertinib monotherapy** (Grade 1A): Standard of care, best risk-benefit
   - **Osimertinib + chemotherapy** (Grade 1B): Enhanced PFS, higher toxicity
   - **Amivantamab + lazertinib** (Grade 1B): Alternative combination, regulatory status varies

5. **Monitoring & Follow-up**
   - Imaging every 8-12 weeks (RECIST v1.1)
   - CNS MRI at baseline and as indicated
   - Regular lab monitoring and toxicity assessment

6. **Progression Management**
   - Mandatory re-biopsy (tissue + liquid)
   - Identify resistance mechanism (MET amplification, C797S, SCLC transformation)
   - Select second-line therapy based on findings

**Recommendation for This Patient:**
Based on ECOG PS 1, no confirmed brain metastases, and no severe organ dysfunction, **osimertinib 80 mg orally once daily** is the recommended first-line treatment (GRADE 1A, Strong recommendation, High-quality evidence).

---
*Algorithm prepared: 2025-06-15 | Version 1.0 | Evidence-based clinical decision support*
