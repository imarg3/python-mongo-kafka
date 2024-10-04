from bson import ObjectId


def order_to_json(order):
    # Convert ObjectId to string if present
    if isinstance(order, dict):
        order['_id'] = str(order['_id']) if '_id' in order else None
    return order
