import json
import random
import time
from datetime import datetime

users = [f"USR{1000+i}" for i in range(100)]
merchants = [f"MER{200+i}" for i in range(50)]
locations = ["Jaipur", "Delhi", "Mumbai", "Banglore", "Hyderabad", "Pune", "Patna", "Lucknow"]
transaction_types = ["UPI", "CARD", "NETBANKING"]
statuses = ["SUCCESS", "FAILED"]
currencies = ["INR", "DOLLAR"]

def generate_transaction():
    transaction = {
        "transaction_id" : f"TXN{random.randint(100000, 999999)}",
        "user_id" : random.choice(users),
        "amount" : round(random.uniform(10, 120000), 2),
        "currency" : random.choice(currencies),
        "transaction_type" : random.choice(transaction_types),
        "merchant_id" : random.choice(merchants),
        "location" : random.choice(locations),
        "device_id" : f"DEV{random.randint(500, 999)}",
        "status" : random.choices(statuses, weights=[85, 15])[0],
        "event_time" : datetime.utcnow().isoformat()        
    }
    return transaction

while True:
    txn = generate_transaction()
    print(json.dumps(txn))
    time.sleep(2)

