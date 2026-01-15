## Transaction Dataset Schema

Each transaction event is generated in JSON format.

| Column Name | Description |
|------------|-------------|
| transaction_id | Unique transaction identifier |
| user_id | Customer ID |
| amount | Transaction amount |
| currency | Currency type |
| transaction_type | UPI / CARD / NETBANKING |
| merchant_id | Merchant identifier |
| location | Transaction location |
| device_id | Device identifier |
| status | SUCCESS / FAILED |
| event_time | Actual transaction timestamp |

### Notes
- `event_time` is used for windowing and watermarking
- Schema is enforced during stream processing
