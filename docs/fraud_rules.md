## Fraud Detection Rules (Rule-Based)

### Rule 1: High-Value Transactions
    IF amount > 50,000
    → FRAUD_REASON = HIGH_VALUE
    → IS_FRAUD = 1

### Rule 2: Failed High-Value Transaction
    IF amount > 30,000 AND status = 'FAILED'
    → FRAUD_REASON = FAILED_HIGH_VALUE
    → IS_FRAUD = 1

### Rule 3: Location-Based Risk
    IF location IN ('Delhi', 'Mumbai') AND amount > 40,000
    → FRAUD_REASON = GEO_HIGH_RISK
    → IS_FRAUD = 1

### Default Case
    ELSE
    → FRAUD_REASON = NORMAL
    → IS_FRAUD = 0


