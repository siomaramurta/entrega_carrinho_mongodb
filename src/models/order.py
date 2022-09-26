from bson import ObjectId

async def create_order(orders_collection, order):
    try:
        insert_order = await orders_collection.insert_one(order)
        if order.inserted_id:
            insert_order = await get_order(orders_collection, order.inserted_id)
            return insert_order
        print("Create order")
    except Exception as e:
        return f'create_order.error: {e}'

async def get_order(orders_collection, order_id):
    try:
        order = await orders_collection.find_one({'_id': ObjectId(order_id)})
        return order
    except Exception as e:
        return f'get_order.error: {e}'

async def delete_order(orders_collection, order_id):
    try:
        order = orders_collection.delete_one(
            {'_id': ObjectId(order_id)}
        )
        if order.deleted_count:
            return {'status': 'Order deleted successfully'}
    except Exception as e:
        return f'delete_order.error: {e}'