

from kafka import KafkaProducer
import time

kafka_url = "broker.kafka.l4lb.thisdcos.directory:9092"
topic_name = "example_topic"

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))

p = KafkaProducer(bootstrap_servers=kafka_url)

iter_count = 0

while True:
    p.send(topic_name, b"test message - {}".format(iter_count))
    time.sleep(1)

p.flush(30)