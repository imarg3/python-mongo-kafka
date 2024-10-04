from app.domain.interfaces.order_repository import IOrderRepository
import logging

logger = logging.getLogger(__name__)


class MongoOrderRepository(IOrderRepository):
    def __init__(self, mongo_client):
        self.collection = mongo_client['orders']

    def save_order(self, order):
        logger.info(f"Saving order {order['order_id']} to MongoDB.")
        return self.collection.insert_one(order)

    def get_order(self, order_id):
        logger.info(f"Fetching order {order_id} from MongoDB.")
        return self.collection.find_one({"order_id": order_id})

    def get_all_orders(self):
        return list(self.collection.find())
