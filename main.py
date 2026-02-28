import pandas as pd

# Load transaction data
data = pd.read_csv("transactions.csv")
# Convert time column into actual time format
data["time"] = pd.to_datetime(data["time"], format="%H:%M")

# Sort data by user and time
data = data.sort_values(by=["user_id", "time"])

# Display full table
print("All Transactions:")
print(data)
# Detect large transactions
high_transactions = data[data["amount"] > 50000]

print("\nSuspicious High-Value Transactions:")
print(high_transactions)
print("\nRapid Transaction Alerts:")

for user in data["user_id"].unique():
    user_data = data[data["user_id"] == user]
    
    # Calculate time difference between consecutive transactions
    time_diff = user_data["time"].diff()
    
    # If transactions occur within 20 minutes
    rapid = time_diff < pd.Timedelta(minutes=20)
    
    if rapid.sum() >= 2:
        print(f"User {user} has multiple rapid transactions.")