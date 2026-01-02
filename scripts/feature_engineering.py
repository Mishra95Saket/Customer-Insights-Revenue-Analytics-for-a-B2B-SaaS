import pandas as pd

df = pd.read_csv("data/processed/customer_features.csv")

df["engagement_score"] = (
    df["monthly_active_users"] * df["feature_adoption_rate"]
)

df["high_risk_churn"] = (
    (df["engagement_score"] < df["engagement_score"].quantile(0.25)) &
    (df["support_tickets_last_90_days"] > 3)
).astype(int)

df.to_csv("data/processed/customer_features.csv", index=False)
print("Feature engineering complete.")
