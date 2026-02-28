# Transaction Risk Analyzer

A Python-based financial transaction monitoring system that analyzes transaction logs and detects suspicious activity using rule-based anomaly detection.

## Features
- Detects unusually high-value transactions
- Detects rapid repeated transactions by the same user
- Time-based behavior analysis using transaction timestamps
- Processes structured transaction datasets (CSV format)

## Technologies Used
- Python
- Pandas (data analysis library)

## How it Works
1. Loads transaction data from a CSV file
2. Converts timestamps into time format
3. Applies threshold-based detection (high amount)
4. Applies behavior-based detection (rapid transactions)
5. Generates alerts for suspicious activity

## How to Run
1. Install Python
2. Install dependencies:
   pip install pandas
3. Run the program:
   py -3.13 main.py

## Future Improvements
- Database storage of flagged transactions
- Visualization dashboard
- Machine learning-based fraud detection