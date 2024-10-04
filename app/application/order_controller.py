from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService
from app.infrastructure.mongo.mongo_repository import MongoOrderRepository
from app.infrastructure.kafka.kafka_producer import KafkaProducer, KafkaEventPublisher
from app.config import Config
from app.utils.mongo_helper import order_to_json

order_controller = Blueprint('order_controller', __name__)

config = Config()


def create_order_service():
    # Kafka Producer and Event Publisher setup
    kafka_producer = KafkaProducer(config.get_kafka_config().get("topic"))
    event_publisher = KafkaEventPublisher(kafka_producer)
    order_repository = MongoOrderRepository(config.get_mongo_client())
    return OrderService(order_repository, event_publisher)


order_service = create_order_service()


@order_controller.route('/orders', methods=['POST'])
def create_order():
    data = request.json

    if 'order_id' not in data:
        return jsonify({'error': 'Missing key: order_id'}), 400
    if 'product_name' not in data:
        return jsonify({'error': 'Missing key: product_name'}), 400
    if 'quantity' not in data:
        return jsonify({'error': 'Missing key: quantity'}), 400
    if 'price' not in data:
        return jsonify({'error': 'Missing key: price'}), 400

    order_service.create_order(
        data['order_id'],
        data['product_name'],
        data['quantity'],
        data['price']
    )
    return jsonify({"message": "Order created"}), 201


@order_controller.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = order_service.get_order(order_id)
    if order:
        return jsonify(order_to_json(order)), 200
    return jsonify({"error": "Order not found"}), 404


@order_controller.route('/orders', methods=['GET'])
def get_all_orders():
    orders = order_service.get_all_orders()
    print(f"Orders - {[order for order in orders]}")

    # Convert each order to JSON-safe format
    orders_json = [order_to_json(order) for order in orders]

    return jsonify(orders_json), 200
