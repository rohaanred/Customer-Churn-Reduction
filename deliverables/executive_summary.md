# Executive Summary: Customer Churn Reduction

## What Was the Problem?
A telecom company was losing customers at an alarming rate - 26.5% annually. That's roughly $1.67M in revenue walking out the door every year. The CEO wanted to know why this was happening and what we could do about it.

## What I Did
I joined a small team (3 people) working with the VP of Customer Success. My job was to dig into the data and find patterns.

Here's what the analysis involved:
- Pulled and cleaned data for 7,043 customers (SQL + Python)
- Did cohort analysis to see when customers typically leave
- Segmented customers by risk level
- Built some basic financial models to estimate the cost of churn

## What I Found
The data told some interesting stories:

1. **Contract type is huge** - Customers on month-to-month plans churn at 42.7%, while those on 2-year contracts only churn at 2.8%. This was the single biggest factor.

2. **First month make or break** - 62% of customers who leave do so in the first 30 days. That's a massive red flag for onboarding.

3. **Fiber optic customers are unhappy** - They churn at 41.9% vs 19% for DSL. Not sure if it's pricing or service quality, but something's off.

4. **Price isn't what I expected** - Churned customers actually pay $13.17 more per month. I initially thought cheaper plans would churn more, but that wasn't the case.

## What I Recommended
1. **Fix the onboarding** - A 30-day guided setup could reduce first-month churn by 40%
2. **Push annual contracts** - Offer discounts to convert month-to-month users
3. **Investigate fiber issues** - Need to understand why these customers are leaving

## Projected Impact
If these recommendations work:
- Churn could drop from 26.5% to around 18%
- That's roughly $534K in annual savings

## Honest Assessment
This was a good learning project, but there are limitations:
- It's based on a public dataset, so results might vary in the real world
- The recommendations are high-level - you'd need A/B testing to validate them
- I didn't build any predictive models, which would be the next step

## Skills Used
- SQL and Python for data analysis
- Excel for financial modeling
- Power BI for visualizations
- Basic cohort analysis techniques
