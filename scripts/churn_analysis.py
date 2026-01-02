import pandas as pd

df = pd.read_csv("data/processed/customer_features.csv")

churn_summary = df.groupby("churned").agg({
    "engagement_score": "mean",
    "support_tickets_last_90_days": "mean",
    "mrr": "mean"
})

print("Churn Insights:")
print(churn_summary)
