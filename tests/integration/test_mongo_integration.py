import pytest
from app.infrastructure.mongo.mongo_repository import MongoOrderRepository
from app.infrastructure.mongo.mongo_factory import MongoFactory


@pytest.fixture
def mongo_repo():
    client = MongoFactory.create()
    return MongoOrderRepository(client)


def test_save_order(mongo_repo):
    order = {'order_id': '1', 'product_name': 'Product A', 'quantity': 2, 'price': 100}
    result = mongo_repo.save_order(order)
    assert result.inserted_id is not None


def test_get_order(mongo_repo):
    order_id = '1'
    order = mongo_repo.get_order(order_id)
    assert order['order_id'] == order_id
