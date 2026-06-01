# Market Basket Analysis Explanation

This project uses association rule mining to find products that are frequently purchased together.

## Workflow

1. Load retail transaction dataset.
2. Clean missing product descriptions.
3. Remove invalid quantities.
4. Group products by invoice number.
5. Convert transactions into basket format.
6. Apply Apriori algorithm.
7. Extract association rules using support, confidence, and lift.

## Example Rule

If a customer buys Product A, they are likely to buy Product B.

Metrics:
- Support
- Confidence
- Lift
