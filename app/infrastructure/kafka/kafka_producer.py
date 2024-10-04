import json
from app.infrastructure.kafka.kafka_factory import KafkaFactory
import logging
from app.domain.interfaces.event_publisher import DomainEventPublisher

logger = logging.getLogger(__name__)


class KafkaProducer:
    def __init__(self, topic):
        self.producer = KafkaFactory().create_producer()
        self._topic = topic

    def send(self, key, value):
        try:
            self.producer.produce(self._topic, key=key, value=json.dumps(value))
            self.producer.flush()  # Ensure all messages are sent
            logger.info(f"Message sent to Kafka: {key} -> {value}")
        except Exception as e:
            logger.error(f"Failed to send message to Kafka: {e}")

    def get_topic(self):
        return self._topic


class KafkaEventPublisher(DomainEventPublisher):
    def __init__(self, kafka_producer):
        self.kafka_producer = kafka_producer

    def publish_event(self, event):
        print(f"Event: {event}")
        print(event.get('order_id'))
        self.kafka_producer.send(key=event.get('order_id'), value=event)
