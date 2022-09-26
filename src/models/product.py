from bson import ObjectId

async def create_product(products_collection, product):
    try:
        product = products_collection.insert_one(product)
        if product.inserted_id:
            product = await get_product(products_collection, product.inserted_id)
            return product
    except Exception as e:
        print(f'create_product.error: {e}')


async def get_product(products_collection, product_id):
    try:
        product = await products_collection.find_one({'_id': ObjectId(product_id)})
        if product:
            return product
    except Exception as e:
        print(f'get_product.error: {e}')


async def delete_product(products_collection, product_id):
    try:
        product = await products_collection.delete_one(
            {'_id': ObjectId(product_id)}
        )
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')