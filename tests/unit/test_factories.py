from app.infrastructure.mongo.mongo_factory import MongoFactory
from app.infrastructure.kafka.kafka_factory import KafkaFactory


def test_mongo_factory_creation():
    client = MongoFactory.create()
    assert client is not None


def test_kafka_producer_creation():
    producer = KafkaFactory.create_producer()
    assert producer is not None


def test_kafka_consumer_creation():
    consumer = KafkaFactory.create_consumer()
    assert consumer is not None
