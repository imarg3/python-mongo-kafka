import pytest
from unittest.mock import Mock
from app.services.order_service import OrderService


@pytest.fixture
def order_service():
    order_repository = Mock()
    event_publisher = Mock()
    return OrderService(order_repository, event_publisher)


def test_create_order(order_service):
    order_service.create_order('1', 'Product A', 2, 100)
    order_service.order_repository.save_order.assert_called_once()
    order_service.event_publisher.publish_event.assert_called_once()


def test_get_order(order_service):
    order_service.order_repository.get_order.return_value = {'order_id': '1', 'product_name': 'Product A'}
    order = order_service.get_order('1')
    assert order['order_id'] == '1'
