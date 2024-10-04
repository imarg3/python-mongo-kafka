from flask import Flask
from logging.handlers import RotatingFileHandler
import logging
import threading
from app.application.order_controller import order_controller
from app.config import Config
from app.infrastructure.kafka.kafka_consumer import KafkaConsumer


def create_app():
    app = Flask(__name__)

    # Set up logging to a file with rotation
    if not app.debug:  # Only configure this in non-debug mode (production)
        handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
        handler.setLevel(logging.INFO)  # Adjust level as needed (e.g., INFO, ERROR)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)
    # Load configuration based on environment
    app_config = Config()
    app.config['DEBUG'] = app_config.get('DEBUG', False)

    # Kafka Consumer
    def handle_kafka_message(message):
        # Add your logic to process the Kafka message
        print(f"Processing Kafka message: {message}")
        # For example, you might want to store this message in the database

    def start_kafka_consumer():
        kafka_consumer = KafkaConsumer()
        kafka_consumer.subscribe(handle_kafka_message)

    def run_kafka_consumer():
        print("Kafka consumer starting ...")
        consumer_thread = threading.Thread(target=start_kafka_consumer)
        consumer_thread.daemon = True  # Ensure it exits when the main program exits
        consumer_thread.start()

    @app.route('/')
    def index():
        return f"Debug: {app.config['DEBUG']}"

    app.register_blueprint(order_controller)

    run_kafka_consumer()

    return app
