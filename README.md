# Superstore Sales Data Analysis

---

## Introduction

This project analyzes a commercial dataset to identify key factors influencing sales profitability.

The goal is to apply data analysis techniques using Pandas and data visualization with Plotly, with a strong business-oriented perspective.

---

## Objectives

- Identify the most profitable periods  
- Detect loss periods  
- Understand which product categories drive profit  
- Explore the impact of discounts on profitability  

---

## Dataset

- Source: Superstore dataset  
- Includes:
  - Order dates  
  - Product categories  
  - Profit  
  - Discounts  

---

## Methodology

### Data Cleaning
- Converted date columns using `pd.to_datetime(errors='coerce')`
- Handled invalid or missing values  

### Data Transformation
- Extracted Year and Month from order dates  
- Aggregated data using `groupby`  
- Restructured data with `reset_index` for visualization  

### Data Analysis
- Profit by category  
- Profit over time (monthly)  
- Focused analysis on key periods:
  - March 2013 (peak)
  - May 2014 (loss)  
- Analysis of discount impact on profit  

### Data Visualization
- Monthly profit evolution (line chart)  
- Profit by category (bar chart)  
- Mini dashboard combining both views  

---

## Key Findings

- 2013 is the most profitable year  
- March 2013 shows a significant profit peak  
- This peak is mainly driven by the Technology category  
- May 2014 shows a notable loss  
- Losses are linked to Furniture and Technology categories  
- Technology remains the most profitable category overall  
- Discounts appear to negatively impact profitability  

---

## Business Insight

May 2014 represents an isolated loss that does not repeat across the dataset.

The analysis suggests that high discounts may have reduced profitability, leading to negative results in some categories.

Since Technology remains the most profitable category overall, this issue is likely due to a temporary pricing strategy rather than a structural problem.

---

## Dashboard

The project includes a mini dashboard built with Plotly.

![Dashboard](images/dashboard.png)

---

## Technologies

- Python  
- Pandas  
- Plotly  

---

## Conclusion

This project highlights the importance of exploratory data analysis in understanding business performance.

It demonstrates how specific periods and business decisions (such as discount strategies) can significantly impact profitability.

---

---

## Version française (résumé)

---

## Introduction

Ce projet analyse un dataset commercial afin d’identifier les facteurs influençant la rentabilité.

---

## Objectifs

- Identifier les périodes rentables et déficitaires  
- Comprendre l’impact des catégories  
- Analyser l’effet des remises sur le profit  

---

## Résultats principaux

- 2013 est l’année la plus rentable  
- Mars 2013 présente un pic de profit important  
- Mai 2014 montre une perte significative  
- Les catégories Furniture et Technology sont impactées  
- Technology reste globalement la plus rentable  
- Les remises influencent négativement le profit  

---

## Analyse

La perte observée en mai 2014 semble liée à une politique de remises trop agressive.

Cette situation reste ponctuelle et ne remet pas en cause la rentabilité globale.

---

## Conclusion

Ce projet montre l’importance de l’analyse de données pour comprendre les performances commerciales et orienter les décisions stratégiques.
