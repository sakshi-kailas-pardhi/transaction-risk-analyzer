# Transaction Risk Analyzer

A rule-based fraud detection system that analyzes financial transaction logs and flags suspicious activities.

## Features
- Detects unusually high-value transactions
- Identifies rapid repeated transactions by the same user
- Detects impossible travel (transactions from different cities within short time)
- Logs suspicious transactions into a SQLite database for analysis

## Technologies Used
- Python
- Pandas
- SQLite

## How it Works
1. Loads transaction data from a CSV file
2. Processes user transactions chronologically
3. Applies fraud detection rules
4. Stores flagged alerts in a database

## Use Case
Simulates how financial institutions monitor transactions to detect fraud patterns.
