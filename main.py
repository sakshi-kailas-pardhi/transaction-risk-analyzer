import pandas as pd
import sqlite3

# Load transaction data
data = pd.read_csv("transactions.csv")

# Connect to database (creates file if not exists)
conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()
# Create table for flagged transactions
cursor.execute("""
CREATE TABLE IF NOT EXISTS flagged_transactions (
    user_id TEXT,
    amount INTEGER,
    location TEXT,
    time TEXT,
    reason TEXT
)
""")
conn.commit()
cursor.execute("DELETE FROM flagged_transactions")
conn.commit()

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
# Store high-value transactions
for _, row in high_transactions.iterrows():
    cursor.execute(
        "INSERT INTO flagged_transactions VALUES (?, ?, ?, ?, ?)",
        (row["user_id"], row["amount"], row["location"], str(row["time"]), "High Value Transaction")
    )
conn.commit()


print("\nRapid Transaction Alerts:")

for user in data["user_id"].unique():
    user_data = data[data["user_id"] == user]
    
    # Calculate time difference between consecutive transactions
    time_diff = user_data["time"].diff()
    
    # If transactions occur within 20 minutes
    rapid = time_diff < pd.Timedelta(minutes=20)
    
    if rapid.sum() >= 2:
        print(f"User {user} has multiple rapid transactions.")
        # Get only rapid transactions
        rapid_transactions = user_data[rapid]

        for _, row in rapid_transactions.iterrows():
         cursor.execute(
        "INSERT INTO flagged_transactions VALUES (?, ?, ?, ?, ?)",
        (row["user_id"], row["amount"], row["location"], str(row["time"]), "Rapid Transactions")
    )
        conn.commit()

        
         # Detect impossible travel
location_change = user_data["location"] != user_data["location"].shift()
impossible_travel = (time_diff < pd.Timedelta(minutes=60)) & location_change

impossible_transactions = user_data[impossible_travel]

for _, row in impossible_transactions.iterrows():
    cursor.execute(
        "INSERT INTO flagged_transactions VALUES (?, ?, ?, ?, ?)",
        (row["user_id"], row["amount"], row["location"], str(row["time"]), "Impossible Travel")
    )

conn.commit()



print("\nStored Alerts in Database:")
for row in cursor.execute("SELECT * FROM flagged_transactions"):
    print(row)