import json
from kafka import KafkaProducer
from pub.pub import pub


class Producer:
    def __init__(self):
        self.producer = None
        self.pub = pub()
        self.message_s1= None
        self.message_s2 = None


    def conn(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8')
                                    )

    def get_interesting(self):
        return self.pub.get_interesting()

    def get_not_interesting(self):
        return self.pub.get_not_interesting()

    def send_message(self, topic, message):
        if not self.producer:
            self.conn()
        self.producer.send(topic, message)
        print("נשלח:",message, "to", topic)
        self.close_conn()

    def close_conn(self):
        self.producer.close()
