import pandas as pd

df = pd.read_csv("data/processed/customer_features.csv")

upgrade_analysis = df.groupby("upgraded").agg({
    "engagement_score": "mean",
    "tenure_months": "mean",
    "mrr": "mean"
})

print("Revenue Expansion Insights:")
print(upgrade_analysis)
