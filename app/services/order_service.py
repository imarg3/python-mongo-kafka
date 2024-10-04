from app.domain.models.order import Order
from app.domain.interfaces.order_repository import IOrderRepository
from app.domain.interfaces.event_publisher import DomainEventPublisher
import logging

logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self, order_repository: IOrderRepository, event_publisher: DomainEventPublisher):
        self.order_repository = order_repository
        self.event_publisher = event_publisher

    def create_order(self, order_id, product_name, quantity, price):
        order = Order(order_id, product_name, quantity, price)
        self.order_repository.save_order(order.to_dict())
        logger.info(f"Order {order_id} created.")

        # Publish event after saving the order
        self.event_publisher.publish_event(order.to_dict())

    def get_order(self, order_id):
        return self.order_repository.get_order(order_id)

    def get_all_orders(self):
        return self.order_repository.get_all_orders()
