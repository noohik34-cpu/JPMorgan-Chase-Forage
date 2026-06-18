import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Features
X = df[
    [
        "credit_lines_outstanding",
        "loan_amt_outstanding",
        "total_debt_outstanding",
        "income",
        "years_employed",
        "fico_score"
    ]
]

# Target
y = df["default"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, predictions))

# Example Customer
new_customer = [[
    2,      # credit_lines_outstanding
    5000,   # loan_amt_outstanding
    3000,   # total_debt_outstanding
    60000,  # income
    5,      # years_employed
    650     # fico_score
]]

# Probability of Default
pd_value = model.predict_proba(new_customer)[0][1]

print("Probability of Default:", round(pd_value, 4))

# Expected Loss
loan_amount = 5000

expected_loss = pd_value * loan_amount * 0.9

print("Expected Loss:", round(expected_loss, 2))
