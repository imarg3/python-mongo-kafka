from confluent_kafka import KafkaException
from app.infrastructure.kafka.kafka_factory import KafkaFactory
from app.config import Config
import json
import logging
from app.domain.interfaces.event_consumer import DomainEventConsumer

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)  # Set the log level (DEBUG, INFO, WARNING, ERROR)
logger = logging.getLogger(__name__)  # Create a logger object


class KafkaConsumer(DomainEventConsumer):
    def __init__(self):
        self.consumer = KafkaFactory().create_consumer()

    def subscribe(self, callback):
        topic = Config().get_kafka_config().get("topic")
        print(f"Consuming from topic: {topic}")
        self.consumer.subscribe([topic])

        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)  # Poll Kafka for new messages
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())
                else:
                    message = json.loads(msg.value().decode('utf-8'))
                    print(f"Consumed message: {message}")
                logger.info(f"Received event from {topic}: {msg.value().decode('utf-8')}")
                callback(json.loads(msg.value().decode('utf-8')))
        except Exception as e:
            logger.error(f"Error consuming messages: {e}")
        finally:
            self.consumer.close()
