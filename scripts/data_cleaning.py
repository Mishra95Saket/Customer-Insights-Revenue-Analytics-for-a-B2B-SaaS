import pandas as pd

df = pd.read_csv("data/raw/saas_customers.csv")

df = df.drop_duplicates()
df = df[df["tenure_months"] > 0]

df.to_csv("data/processed/customer_features.csv", index=False)
print("Cleaned dataset saved.")
