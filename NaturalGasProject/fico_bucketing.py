import pandas as pd

# Load data
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Create 5 FICO buckets
df["rating"] = pd.qcut(
    df["fico_score"],
    q=5,
    labels=[5, 4, 3, 2, 1]
)

print("\nFICO Rating Map\n")
print(df[["fico_score", "rating"]].head(20))

# Bucket boundaries
bins = pd.qcut(
    df["fico_score"],
    q=5,
    retbins=True,
    duplicates="drop"
)[1]

print("\nBucket Boundaries:")
print(bins)