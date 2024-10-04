from confluent_kafka import Producer, Consumer
from app.config import Config


class KafkaFactory:
    @staticmethod
    def create_producer():
        kafka_config = Config().get_kafka_config()
        producer_config = kafka_config.get('producer', {})
        return Producer({
            'bootstrap.servers': kafka_config.get('bootstrap.servers'),
            'security.protocol': kafka_config.get('security.protocol'),
            'sasl.mechanism': kafka_config.get('sasl.mechanism'),
            'sasl.username': kafka_config.get('sasl.username'),
            'sasl.password': kafka_config.get('sasl.password'),
            **producer_config
        })

    @staticmethod
    def create_consumer():
        kafka_config = Config().get_kafka_config()
        consumer_config = kafka_config.get('consumer', {})
        print(f"Consumer Config: {consumer_config}")

        return Consumer({
            'bootstrap.servers': kafka_config.get('bootstrap.servers'),
            'security.protocol': kafka_config.get('security.protocol'),
            'sasl.mechanism': kafka_config.get('sasl.mechanism'),
            'sasl.username': kafka_config.get('sasl.username'),
            'sasl.password': kafka_config.get('sasl.password'),
            **consumer_config
        })
