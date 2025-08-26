from kafka import KafkaConsumer
from interesting.manager import Manager
import json

manager = Manager()

consumer = KafkaConsumer(
    'interesting',
    bootstrap_servers='localhost:9092',
    group_id='my-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("interesting מקשיב להודעות...")

for message in consumer:
    manager.insert_data_to_db(message.value)
    print("התקבלה הודעה:", message.value)