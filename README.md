# Analyse de données commerciales – Superstore

---

## 🇫🇷 Version Française

---

## Introduction

Ce projet consiste à analyser un jeu de données commerciales afin d’identifier les facteurs influençant la rentabilité des ventes.

L’objectif est de mettre en pratique des compétences en manipulation de données avec **Pandas** et en visualisation avec **Plotly**, dans une logique d’analyse métier.

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
  - `Year`
  - `Month`
- Agrégation des données avec `groupby`

### 3. Analyse
- Profit par catégorie  
- Profit par année  
- Profit mensuel  
- Analyse ciblée de périodes spécifiques  

### 4. Visualisation
- Graphique de l’évolution du profit mensuel (Plotly)

---

## Visualisations

- Évolution du profit dans le temps (mensuel)
- Identification des pics et des creux de performance

---

## Key Findings

- L’année **2013 est la plus rentable**
- Le mois de **mars 2013 présente un pic exceptionnel de profit**
- Ce pic est principalement dû à la catégorie **Technology**
- Le mois de **mai 2014 montre une perte significative**
- Les pertes sont liées aux catégories **Furniture** et **Technology**
- La rentabilité varie fortement selon les périodes
- Les remises (**Discount**) pourraient avoir un impact négatif sur le profit

---

## Axes d’amélioration (Travail restant)

- Analyser l’impact des **remises (Discount) sur le profit**
- Étudier les **sous-catégories (Sub-Category)** pour affiner l’analyse
- Ajouter d’autres visualisations :
  - Profit par catégorie (bar chart)
  - Discount vs Profit
- Améliorer la narration visuelle (dashboard plus complet)
- Optimiser la gestion des valeurs manquantes

---

## 🏁 Conclusion

Ce projet met en évidence l’importance de l’analyse exploratoire pour comprendre la performance commerciale.

Il montre que certaines périodes peuvent fortement impacter la rentabilité, et qu’une analyse plus fine est nécessaire pour identifier les causes précises.

---

---

## 🇬🇧 English Version

---

## Introduction

This project focuses on analyzing a commercial dataset to identify key factors influencing sales profitability.

The goal is to apply data analysis skills using **Pandas** and **Plotly**, with a strong business-oriented approach.

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
  - `Year`
  - `Month`
- Aggregating data with `groupby`

### 3. Analysis
- Profit by category  
- Profit by year  
- Monthly profit trends  
- Focused analysis on specific periods  

### 4. Visualization
- Monthly profit evolution using Plotly

---

## Visualizations

- Profit evolution over time (monthly)
- Identification of peaks and low-performance periods

---

## Key Findings

- **2013 is the most profitable year**
- **March 2013 shows a significant profit peak**
- This peak is mainly driven by the **Technology category**
- **May 2014 shows a significant loss**
- Losses are linked to **Furniture and Technology**
- Profitability varies significantly over time
- **Discounts may negatively impact profit**

---

## Future Improvements

- Analyze the impact of **Discount on Profit**
- Explore **Sub-Categories** for deeper insights
- Add more visualizations:
  - Profit by category (bar chart)
  - Discount vs Profit
- Improve storytelling (dashboard approach)
- Optimize missing data handling

---

## 🏁 Conclusion

This project highlights the importance of exploratory data analysis in understanding business performance.

It shows that certain periods can significantly impact profitability and that deeper analysis is required to identify root causes.
