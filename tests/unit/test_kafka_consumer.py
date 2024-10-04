import pytest
from unittest.mock import Mock, patch
from confluent_kafka import Consumer
from app.infrastructure.kafka.kafka_consumer import KafkaConsumer


@pytest.fixture
def mock_consumer():
    mock = Mock(spec=Consumer)
    mock.poll.return_value = None
    return mock


@pytest.fixture
def kafka_consumer(mock_consumer):
    return KafkaConsumer()


def test_consume_message(kafka_consumer):
    def callback(message):
        assert message == {"order_id": "1234", "status": "created"}

    # Mock the poll method to simulate receiving a message
    message = Mock()
    message.value.return_value.decode.return_value = '{"order_id": "1234", "status": "created"}'
    kafka_consumer.consumer.poll.return_value = message

    kafka_consumer.subscribe(callback)
    kafka_consumer.consumer.poll.assert_called()
