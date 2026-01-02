import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/processed/customer_features.csv")

features = df[[
    "tenure_months",
    "monthly_active_users",
    "feature_adoption_rate",
    "mrr"
]]

X = StandardScaler().fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=42)
df["segment"] = kmeans.fit_predict(X)

df.to_csv("data/processed/customer_features.csv", index=False)
print("Customer segmentation complete.")
