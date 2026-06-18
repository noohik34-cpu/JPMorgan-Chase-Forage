import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Load CSV
df = pd.read_csv("Nat_Gas.csv")

# Convert Date column
df["Dates"] = pd.to_datetime(df["Dates"])

# Plot graph
plt.figure(figsize=(12,5))
plt.plot(df["Dates"], df["Prices"], marker="o")
plt.title("Natural Gas Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()

# Interpolation model
x = df["Dates"].map(pd.Timestamp.toordinal)
y = df["Prices"]

interp_model = interp1d(
    x,
    y,
    kind="linear",
    fill_value="extrapolate"
)

# Monthly averages
df["Month"] = df["Dates"].dt.month

monthly_avg = (
    df.groupby("Month")["Prices"]
    .mean()
)

def estimate_price(date):

    target = pd.to_datetime(date)

    if target <= df["Dates"].max():
        return float(
            interp_model(
                target.toordinal()
            )
        )

    return float(
        monthly_avg[target.month]
    )

print("Historical Price:")
print(estimate_price("2023-06-15"))

print("\nFuture Price:")
print(estimate_price("2025-03-15"))