"""
Customer Churn Analysis - Telco Dataset
Using IBM Telco Customer Churn data from Kaggle

This script analyzes why customers leave and identifies key churn drivers.
"""

import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/telco_customer_churn.csv')

print("=" * 60)
print("CUSTOMER CHURN ANALYSIS")
print("=" * 60)

# 1. Overall Churn Rate
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print(f"\n1. OVERALL CHURN RATE: {churn_rate['Yes']:.1f}%")
print(f"   Total Customers: {len(df):,}")
print(f"   Churned Customers: {(df['Churn'] == 'Yes').sum():,}")

# 2. Churn by Contract Type
print("\n2. CHURN BY CONTRACT TYPE:")
contract_churn = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).round(1)
for contract, rate in contract_churn.items():
    print(f"   {contract}: {rate}%")

# 3. Churn by Tenure (First 12 months)
print("\n3. CHURN BY TENURE (First 12 Months):")
tenure_churn = df[df['tenure'] <= 12].groupby('tenure')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).round(1)
for tenure, rate in tenure_churn.items():
    print(f"   Month {tenure}: {rate}%")

# 4. Churn by Internet Service
print("\n4. CHURN BY INTERNET SERVICE:")
internet_churn = df.groupby('InternetService')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100).round(1)
for service, rate in internet_churn.items():
    print(f"   {service}: {rate}%")

# 5. Monthly Charges Analysis
print("\n5. MONTHLY CHARGES ANALYSIS:")
charges_stats = df.groupby('Churn')['MonthlyCharges'].describe().round(2)
print(f"   Churned Customers Avg: ${charges_stats.loc['Yes', 'mean']}")
print(f"   Retained Customers Avg: ${charges_stats.loc['No', 'mean']}")
print(f"   Difference: ${charges_stats.loc['Yes', 'mean'] - charges_stats.loc['No', 'mean']:.2f}")

# 6. Key Insights
print("\n6. KEY INSIGHTS:")
print(f"   - Month-to-month customers churn at {contract_churn['Month-to-month']}% (vs {contract_churn['Two year']}% for 2-year)")
print(f"   - First-month customers have {tenure_churn[1]}% churn rate")
print(f"   - Fiber optic users churn at {internet_churn['Fiber optic']}% (vs {internet_churn['DSL']}% for DSL)")
print(f"   - Churned customers pay ${charges_stats.loc['Yes', 'mean'] - charges_stats.loc['No', 'mean']:.2f} more per month")

# 7. Financial Impact
monthly_revenue_lost = df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()
annual_revenue_lost = monthly_revenue_lost * 12
print(f"\n7. FINANCIAL IMPACT:")
print(f"   Monthly Revenue Lost: ${monthly_revenue_lost:,.2f}")
print(f"   Annual Revenue Lost: ${annual_revenue_lost:,.2f}")

# TODO: Add predictive modeling (logistic regression or random forest)
# TODO: Add time-series analysis if we get date-level data
# TODO: Run A/B tests on the recommendations
