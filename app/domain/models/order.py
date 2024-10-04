from dataclasses import dataclass


@dataclass(frozen=True)
class OrderId:
    value: str


@dataclass
class Order:
    order_id: OrderId
    product_name: str
    quantity: int
    price: float

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "price": self.price
        }
