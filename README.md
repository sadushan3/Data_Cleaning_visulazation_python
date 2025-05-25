# 📊 Netflix Data Cleaning & Visualization Project

This project shows how to clean and visualize a real-world-style dataset using Python, pandas, numpy, and matplotlib. It’s perfect for portfolios, college submissions, or data analytics practice.

---

## 📁 Dataset Overview

- **500 Netflix-style show entries**
- Columns:
  - `Title`
  - `Genre`
  - `Release_Year`
  - `Seasons`
  - `Rating`
  - `Viewership_Millions`
- Contains intentional **missing values** and **blank cells**

---

## 🧹 Data Cleaning (`clean_netflix_data.py`)

### Steps:
1. Convert blank spaces/tabs to NaN
2. Fill numeric columns with **mean**
3. Fill categorical columns with **mode**
4. Save the cleaned version to `netflix_500_cleaned_dataset.csv`

> Run it:
```bash
python clean_netflix_data.py
