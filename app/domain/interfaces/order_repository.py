from abc import ABC, abstractmethod


class IOrderRepository(ABC):
    @abstractmethod
    def save_order(self, order):
        pass

    @abstractmethod
    def get_order(self, order_id):
        pass

    @abstractmethod
    def get_all_orders(self):
        pass
