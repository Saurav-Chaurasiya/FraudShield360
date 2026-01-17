import json
import random
import time
from datetime import datetime
from datetime import timezone
from azure.eventhub import EventHubProducerClient, EventData, TransportType

CONNECTION_STR = "Endpoint=sb://fraudshield-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=N9hyb8yOlniucWYAO2rEz4y4R59UCWq/1+AEhBUHjWI="
EVENT_HUB_NAME = "transactions-hub"

producer = EventHubProducerClient.from_connection_string(
    conn_str=CONNECTION_STR,
    eventhub_name=EVENT_HUB_NAME,
    transport_type=TransportType.AmqpOverWebsocket
)

def generate_transaction():
    return {
        "transaction_id": f"TXN{random.randint(100000, 999999)}",
        "user_id": f"USR{random.randint(1000, 1100)}",
        "amount": round(random.uniform(10, 120000), 2),
        "currency": "INR",
        "transaction_type": random.choice(["UPI", "CARD", "NETBANKING"]),
        "merchant_id": f"MER{random.randint(200, 250)}",
        "location": random.choice(["Delhi", "Mumbai", "Pune"]),
        "device_id": f"DEV{random.randint(500, 900)}",
        "status": random.choice(["SUCCESS", "FAILED"]),
        "event_time": datetime.now(timezone.utc).isoformat()
    }

while True:
    event = generate_transaction()
    producer.send_event(EventData(json.dumps(event)))
    print("Sent:", event)
    time.sleep(2)
