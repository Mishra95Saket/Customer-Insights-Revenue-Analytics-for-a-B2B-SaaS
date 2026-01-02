### @author - Saket Mishra

# Customer Insights & Revenue Analytics for a B2B SaaS 

## 📌 Project Overview
This project demonstrates an end-to-end Customer Insights Analytics workflow for a B2B SaaS company.  
The goal is to understand **customer behavior**, **churn risk**, and **revenue expansion opportunities** using a fully synthetic dataset designed to mimic real SaaS usage and billing patterns.

This project is structured to reflect:
- Business question formulation
- Behavioral segmentation
- Churn & retention analysis
- Revenue growth insights
- Actionable recommendations for Product, Sales, and Customer Success teams

---

## 🎯 Key Business Questions

### 1️⃣ Which customer segments drive the highest revenue and engagement?
- Identify high-value customer segments using usage, tenure, and plan data
- Inform Sales and Customer Success prioritization

### 2️⃣ What behavioral patterns indicate churn risk?
- Analyze churned vs retained customers
- Identify leading churn indicators (usage drop, support tickets, low feature adoption)

### 3️⃣ What factors influence revenue expansion (upsell & cross-sell)?
- Understand which behaviors precede plan upgrades
- Support data-driven expansion strategies

### 4️⃣ How does product usage correlate with retention and revenue?
- Evaluate feature adoption vs churn
- Inform Product roadmap decisions

---

## 🧠 Dataset Description
The dataset is **synthetically generated** to replicate real SaaS customer data, including:
- Subscription plans
- Monthly recurring revenue (MRR)
- Product usage metrics
- Support interactions
- Churn and expansion behavior

No external or open-source datasets are used.

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- YAML for configuration

---

## 🚀 How to Run the Project

```bash
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python scripts/data_cleaning.py
python scripts/feature_engineering.py
python scripts/exploratory_analysis.py
python scripts/customer_segmentation.py
python scripts/churn_analysis.py
python scripts/revenue_expansion_analysis.py
