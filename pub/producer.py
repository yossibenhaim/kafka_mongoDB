import json
from kafka import KafkaProducer
from pub import pub

# יוצרים producer שמתחבר ל-broker מקומי
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8')
                         )

pub = pub()

message_s1 = pub.get_interesting()
message_s2 = pub.get_not_interesting()

producer.send('interesting', message_s1)
print("נשלח:",message_s1)


producer.send('not_interesting', message_s2)
print("נשלח:",message_s2)


producer.close()

