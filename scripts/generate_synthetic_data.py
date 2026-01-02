import pandas as pd
import numpy as np
import yaml
from datetime import datetime

np.random.seed(42)

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

n = config["data"]["num_customers"]

plans = list(config["plans"].keys())
plan_prices = config["plans"]

df = pd.DataFrame({
    "customer_id": range(1, n + 1),
    "plan": np.random.choice(plans, n, p=[0.5, 0.35, 0.15]),
    "tenure_months": np.random.randint(1, 36, n),
    "monthly_active_users": np.random.poisson(15, n),
    "feature_adoption_rate": np.random.uniform(0.2, 1.0, n),
    "support_tickets_last_90_days": np.random.poisson(2, n),
    "churned": np.random.choice([0, 1], n, p=[0.82, 0.18]),
    "upgraded": np.random.choice([0, 1], n, p=[0.88, 0.12])
})

df["mrr"] = df["plan"].map(plan_prices)
df["last_activity_score"] = (
    df["monthly_active_users"] * df["feature_adoption_rate"]
)

df.to_csv("data/raw/saas_customers.csv", index=False)
print("Synthetic SaaS customer dataset generated.")
