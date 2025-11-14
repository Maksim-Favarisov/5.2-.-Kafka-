# init_producer.py
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

users = ["alice", "bob", "carol", "dave"]

while True:
    data = {
        "user": random.choice(users),
        "event": "login",
        "timestamp": time.time() + 3 * 3600 # Добавляем +3 часа, чтобы совпадали часовые пояса с ClickHouse
    }
    producer.send("user_events_data", value=data)
    print("Sent:", data)
    time.sleep(1)




