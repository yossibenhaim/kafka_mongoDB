from kafka import KafkaConsumer
from not_interesting.manager import Manager
import json

manager = Manager()

consumer = KafkaConsumer(
    'not_interesting',
    bootstrap_servers='broker:9092',
    api_version=(0, 11, 5),
    group_id='my-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    request_timeout_ms=100000
)

print("not_interesting מקשיב להודעות...")

for message in consumer:
    manager.insert_data_to_db(message.value)
    print("התקבלה הודעה:", message.value)