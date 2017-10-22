from kafka import KafkaConsumer


#kafka_url = "localhost:9092"
kafka_url = "broker.kafka.l4lb.thisdcos.directory:9092"
kafka_url = "broker-0.kafka.mesos:9843"
topic_name = "example_topic"

print("Connecting to {}".format(kafka_url))
consumer = KafkaConsumer(bootstrap_servers=kafka_url,
                        auto_offset_reset='earliest')
print("Connection complete")
consumer.subscribe(topic_name)
print("Subscribed to topic {}".format(topic_name))

for message in consumer:
    print (message)

consumer.close()
print("Completed reading kafka topic")