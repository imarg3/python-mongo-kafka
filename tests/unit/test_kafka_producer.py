import pytest
from unittest.mock import Mock
from app.infrastructure.kafka.kafka_producer import KafkaProducer, KafkaEventPublisher


@pytest.fixture
def kafka_producer():
    return Mock(spec=KafkaProducer)


@pytest.fixture
def kafka_event_publisher(kafka_producer):
    return KafkaEventPublisher(kafka_producer)


def test_kafka_event_publisher(kafka_event_publisher):
    event_data = {'order_id': '1', 'product_name': 'Product A'}
    kafka_event_publisher.publish_event(event_data)
    # There is no direct assertion; ensure no exceptions are raised
