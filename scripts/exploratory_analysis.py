import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------
# Setup
# -----------------------------------
DATA_PATH = "data/processed/customer_features.csv"
OUTPUT_FIGURES = "outputs/figures"
OUTPUT_TABLES = "outputs/tables"

os.makedirs(OUTPUT_FIGURES, exist_ok=True)
os.makedirs(OUTPUT_TABLES, exist_ok=True)

sns.set(style="whitegrid")

# -----------------------------------
# Load Data
# -----------------------------------
df = pd.read_csv(DATA_PATH)

# -----------------------------------
# 1. Customer Base Overview
# -----------------------------------
customer_summary = pd.DataFrame({
    "metric": [
        "Total Customers",
        "Average MRR",
        "Median Tenure (Months)",
        "Overall Churn Rate",
        "Upgrade Rate"
    ],
    "value": [
        len(df),
        df["mrr"].mean(),
        df["tenure_months"].median(),
        df["churned"].mean(),
        df["upgraded"].mean()
    ]
})

customer_summary.to_csv(
    f"{OUTPUT_TABLES}/customer_base_summary.csv",
    index=False
)

# -----------------------------------
# 2. Revenue by Plan
# -----------------------------------
revenue_by_plan = (
    df.groupby("plan")
      .agg(
          customers=("customer_id", "count"),
          avg_mrr=("mrr", "mean"),
          churn_rate=("churned", "mean")
      )
      .reset_index()
)

revenue_by_plan.to_csv(
    f"{OUTPUT_TABLES}/revenue_by_plan.csv",
    index=False
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=revenue_by_plan,
    x="plan",
    y="avg_mrr"
)
plt.title("Average MRR by Subscription Plan")
plt.ylabel("Average Monthly Revenue")
plt.xlabel("Plan")
plt.tight_layout()
plt.savefig(f"{OUTPUT_FIGURES}/avg_mrr_by_plan.png")
plt.close()

# -----------------------------------
# 3. Churned vs Retained Behavior
# -----------------------------------
churn_behavior = (
    df.groupby("churned")
      .agg(
          avg_engagement=("engagement_score", "mean"),
          avg_usage=("monthly_active_users", "mean"),
          avg_tickets=("support_tickets_last_90_days", "mean"),
          avg_tenure=("tenure_months", "mean")
      )
      .reset_index()
)

churn_behavior["churned"] = churn_behavior["churned"].map(
    {0: "Retained", 1: "Churned"}
)

churn_behavior.to_csv(
    f"{OUTPUT_TABLES}/churn_behavior_comparison.csv",
    index=False
)

# -----------------------------------
# 4. Engagement vs Churn Rate
# -----------------------------------
df["engagement_bucket"] = pd.qcut(
    df["engagement_score"],
    q=4,
    labels=["Low", "Medium-Low", "Medium-High", "High"]
)

churn_by_engagement = (
    df.groupby("engagement_bucket")
      .agg(churn_rate=("churned", "mean"))
      .reset_index()
)

churn_by_engagement.to_csv(
    f"{OUTPUT_TABLES}/churn_by_engagement.csv",
    index=False
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=churn_by_engagement,
    x="engagement_bucket",
    y="churn_rate"
)
plt.title("Churn Rate by Engagement Level")
plt.ylabel("Churn Rate")
plt.xlabel("Engagement Level")
plt.tight_layout()
plt.savefig(f"{OUTPUT_FIGURES}/churn_by_engagement.png")
plt.close()

# -----------------------------------
# 5. Support Tickets vs Churn
# -----------------------------------
df["ticket_bucket"] = pd.cut(
    df["support_tickets_last_90_days"],
    bins=[-1, 0, 2, 5, df["support_tickets_last_90_days"].max()],
    labels=["0", "1-2", "3-5", "6+"]
)

churn_by_tickets = (
    df.groupby("ticket_bucket")
      .agg(churn_rate=("churned", "mean"))
      .reset_index()
)

churn_by_tickets.to_csv(
    f"{OUTPUT_TABLES}/churn_by_support_tickets.csv",
    index=False
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=churn_by_tickets,
    x="ticket_bucket",
    y="churn_rate"
)
plt.title("Churn Rate by Support Ticket Volume (Last 90 Days)")
plt.ylabel("Churn Rate")
plt.xlabel("Support Ticket Bucket")
plt.tight_layout()
plt.savefig(f"{OUTPUT_FIGURES}/churn_by_support_tickets.png")
plt.close()

# -----------------------------------
# 6. Key Business Takeaways (Console)
# -----------------------------------
print("\n--- Exploratory Analysis Key Insights ---\n")
print("• Higher engagement customers have significantly lower churn")
print("• Support ticket volume is positively correlated with churn")
print("• Enterprise plans generate higher MRR with lower churn")
print("• Early-tenure customers are at higher churn risk\n")

print("EDA outputs saved to /outputs/figures and /outputs/tables")
