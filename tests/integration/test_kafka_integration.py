'''
import pytest
from confluent_kafka import Producer, Consumer


@pytest.fixture(scope="module")
def kafka_config():
    return {
        "bootstrap.servers": "localhost:9092",
        "group.id": "test-group",
        "auto.offset.reset": "earliest"
    }


@pytest.fixture(scope="module")
def kafka_producer(kafka_config):
    return Producer(kafka_config)


@pytest.fixture(scope="module")
def kafka_consumer(kafka_config):
    consumer = Consumer(kafka_config)
    consumer.subscribe(["order-events"])
    yield consumer
    consumer.close()


def test_kafka_producer_and_consumer(kafka_producer, kafka_consumer):
    message = {"order_id": "123", "product": "Book", "quantity": 1}
    kafka_producer.produce("order-events", key="123", value=str(message))
    kafka_producer.flush()

    msg = kafka_consumer.poll(timeout=10.0)
    assert msg is not None
    assert msg.key() == b"123"
    assert msg.value() == b"{'order_id': '123', 'product': 'Book', 'quantity': 1}"
'''
