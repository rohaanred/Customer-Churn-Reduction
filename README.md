# Customer Churn Reduction - Telco Dataset

## Overview
This project analyzes customer churn for a telecom company using the IBM Telco Customer Churn dataset from Kaggle. The goal was to understand why customers leave and what can be done to reduce churn.

**Dataset**: 7,043 customers, 21 features
**Source**: [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## What I Did
- Cleaned and explored the data using Python (Pandas)
- Identified key churn drivers through cohort analysis
- Built some basic visualizations in Power BI
- Created recommendations based on the findings

## Key Findings
Here's what stood out from the analysis:

- **Contract type matters a lot** - Month-to-month customers churn at 42.7%, while 2-year contracts are only 2.8%. This was the biggest insight.
- **First month is critical** - 62% of customers who leave do so in the first month. Something's clearly wrong with onboarding.
- **Fiber optic has issues** - These customers churn at 41.9% compared to 19% for DSL. Could be pricing or service quality.
- **Price sensitivity** - Churned customers actually pay $13.17 more on average, which was surprising.

## Financial Impact
- **Monthly revenue lost**: ~$139K
- **Annual revenue lost**: ~$1.67M

## What I'd Do Differently
Honestly, this was a learning project. If I had more time:
- Would've done more feature engineering
- Could've built a predictive model (logistic regression or random forest)
- The recommendations are high-level - in reality, you'd need to run A/B tests to validate them

## Limitations
- Used a public dataset, so findings might not apply to every telecom company
- No time-series data - would be interesting to see churn patterns over seasons
- The financial impact numbers are rough estimates

## Recommendations
1. **Fix onboarding** - The 62% first-month churn is alarming. A guided setup process could help.
2. **Push annual contracts** - Maybe offer discounts to convert month-to-month users.
3. **Look into fiber pricing** - The high churn here suggests customers don't see the value.

## Tools Used
- Python (Pandas, NumPy)
- SQL
- Excel
- Power BI

## What I Learned
- Data cleaning takes way more time than expected
- Cohort analysis is super useful for understanding churn
- Always question your assumptions - I initially thought price was the main driver, but contract type mattered way more
