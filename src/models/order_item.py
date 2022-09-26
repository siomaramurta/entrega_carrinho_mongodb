from models.product import get_product
from models.order import get_order

from bson import ObjectId

async def get_order_item(order_items_collection, order_item_id):
    try:
        order = order_items_collection.find_one(
            {'_id': ObjectId(order_item_id)})
        return order
    except Exception as e:
        return f'get_order_item.error: {e}'


async def get_product_and_order(products_collection, product_id, orders_collection, order_id):
    product = await get_product(products_collection, product_id)
    order = await get_order(orders_collection, order_id)
    return product, order

async def insert_product_cart(products_collection, product_id, orders_collection, order_id, order_items_collection):
    try:
        product, order = await get_product_and_order(products_collection, product_id, orders_collection, order_id)
        if product and order:
            return await create_order_item(order_items_collection, product, order)
    except Exception as e:
        return f'insert_product_cart.error: {e}'

async def create_order_item(order_items_collection):
    try:
        order_item = order_items_collection.insert_one(order_item)
        if order_item.inserted_id:
            response = await get_order_item(order_items_collection, order_item.inserted_id)
            return response
    except Exception as e:
        print(f'create_order_item.error: {e}')

async def get_order_item_sum(order_items_collection, id):
    cart_sum = order_items_collection.aggregate(
        [
            {
                "$group": {
                    "_id": ObjectId(id),
                    "sum_price": {"$sum": "$product.price"},
                }
            }
        ]
    )
    return cart_sum["sum_price"]

async def get_order_items_by_id(order_items_collection, order_id):
    try:
        order = order_items_collection.find_one({"order._id": order_id})
        return order
    except Exception as e:
        return f'get_order_items_by_id.error: {e}'

async def delete_product_from_order_item(product_id, order_items_collection):
    try:
        product = order_items_collection.delete_one(
            {'product_id': ObjectId(product_id)}
        )
        if product.deleted_count:
            return {'status': 'Product deleted successfully'}
    except Exception as e:
        return f'delete_product.error: {e}'