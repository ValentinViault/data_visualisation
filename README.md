# Analyse de données commerciales – Superstore

---

## Version Française

---

## Introduction

Ce projet consiste à analyser un jeu de données commerciales afin d’identifier les facteurs influençant la rentabilité des ventes.

L’objectif est de mettre en pratique des compétences en manipulation de données avec Pandas et en visualisation avec Plotly, dans une logique d’analyse métier.

---

## Objectif

- Identifier les périodes les plus rentables  
- Détecter les périodes de perte  
- Comprendre quelles catégories influencent le profit  
- Explorer les causes possibles des variations de performance  

---

## Dataset

- Source : Superstore dataset  
- Données commerciales contenant :
  - Dates de commande  
  - Catégories de produits  
  - Profit  
  - Remises (Discount)  

---

## Méthodologie

### 1. Nettoyage des données
- Conversion des dates avec `pd.to_datetime(errors='coerce')`
- Gestion des valeurs invalides (NaT)

### 2. Transformation
- Extraction de l’année et du mois :
  - Year
  - Month
- Agrégation des données avec `groupby`

### 3. Analyse
- Profit par catégorie  
- Profit par année  
- Profit mensuel  
- Analyse ciblée de périodes spécifiques (mars 2013, mai 2014)  
- Étude de l’impact des remises sur le profit  

### 4. Visualisation
- Évolution du profit mensuel (line chart)
- Profit par catégorie (bar chart)
- Impact des remises sur le profit (scatter plot)

---

## Visualisations

- Évolution du profit dans le temps (mensuel)
- Comparaison du profit par catégorie
- Analyse de la relation entre Discount et Profit

---

## Key Findings

- L’année 2013 est la plus rentable
- Le mois de mars 2013 présente un pic exceptionnel de profit
- Ce pic est principalement dû à la catégorie Technology
- Le mois de mai 2014 montre une perte significative
- Les pertes sont liées aux catégories Furniture et Technology
- La rentabilité varie fortement selon les périodes
- Les remises (Discount) semblent avoir un impact négatif sur le profit

---

## Analyse approfondie

### Analyse

Le mois de mai 2014 présente une perte isolée, non reproduite sur le reste de la période.

L’analyse de la relation entre les remises (Discount) et le profit suggère que des remises élevées ont pu impacter négativement la rentabilité, certaines transactions devenant déficitaires.

Par ailleurs, la catégorie Technology restant globalement la plus rentable sur l’ensemble du dataset, cette perte semble liée à des conditions commerciales ponctuelles plutôt qu’à un problème structurel.

---

## Recommandations

- Limiter les remises élevées, en particulier sur les produits à faible marge, afin de préserver la rentabilité  
- Surveiller les périodes de faible performance pour identifier rapidement les anomalies  
- Capitaliser sur la catégorie Technology, qui constitue le principal levier de profit  
- Mettre en place un suivi plus précis de l’impact des remises sur le profit  
- Approfondir l’analyse au niveau des sous-catégories pour identifier les segments les plus rentables  

---

## Conclusion

Ce projet met en évidence l’importance de l’analyse exploratoire pour comprendre la performance commerciale.

Il montre que certaines périodes peuvent fortement impacter la rentabilité et qu’une analyse plus fine est nécessaire pour identifier les causes précises.

---

---

## English Version

---

## Introduction

This project focuses on analyzing a commercial dataset to identify key factors influencing sales profitability.

The goal is to apply data analysis skills using Pandas and Plotly, with a strong business-oriented approach.

---

## Objective

- Identify the most profitable periods  
- Detect loss periods  
- Understand which categories drive profit  
- Explore possible causes of performance variations  

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

### 1. Data Cleaning
- Date conversion using `pd.to_datetime(errors='coerce')`
- Handling invalid/missing values

### 2. Transformation
- Extracting:
  - Year
  - Month
- Aggregating data with `groupby`

### 3. Analysis
- Profit by category  
- Profit by year  
- Monthly profit trends  
- Focused analysis on specific periods (March 2013, May 2014)  
- Analysis of discount impact on profit  

### 4. Visualization
- Monthly profit evolution (line chart)
- Profit by category (bar chart)
- Discount vs Profit (scatter plot)

---

## Visualizations

- Profit evolution over time (monthly)
- Profit comparison by category
- Analysis of the relationship between Discount and Profit

---

## Key Findings

- 2013 is the most profitable year
- March 2013 shows a significant profit peak
- This peak is mainly driven by the Technology category
- May 2014 shows a significant loss
- Losses are linked to Furniture and Technology
- Profitability varies significantly over time
- Discounts may negatively impact profit

---

## In-depth Analysis

### Analysis

May 2014 shows an isolated loss that is not observed in other periods.

The analysis of the relationship between discount and profit suggests that high discounts may have negatively impacted profitability, with some transactions becoming unprofitable.

Since the Technology category remains the most profitable overall, this loss appears to be linked to temporary commercial conditions rather than a structural issue.

---

## Recommendations

- Limit high discounts, especially on low-margin products, to preserve profitability  
- Monitor low-performance periods to quickly detect anomalies  
- Leverage the Technology category as a primary profit driver  
- Implement closer tracking of discount impact on profit  
- Perform deeper analysis at the sub-category level to identify the most profitable segments  

---

## Conclusion

This project highlights the importance of exploratory data analysis in understanding business performance.

It shows that certain periods can significantly impact profitability and that deeper analysis is required to identify root causes.
