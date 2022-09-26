from bson import ObjectId

async def create_address(address_collection, address):
    try:
        info_insert_address = await address_collection.insert_one(address)
        if address.inserted_id:
            info_insert_address = await get_addresses(address_collection, address.inserted_id)
            return info_insert_address
    except Exception as e:
        print(f'get_addresses.error: {e}')

async def get_addresses(address_collection, address_id):
    try:
        data = await address_collection.find_one({'_id': ObjectId(address_id)})
        if data:
            return data
    except Exception as e:
        print(f'get_addresses.error: {e}') 
    
async def delete_address(address_collection, address_id):
    try:
        address = address_collection.delete_one(
            {'_id': ObjectId(address_id)}
        )
        if address.deleted_count:
            return {'status': 'Address deleted successfully'}
    except Exception as e:
        return f'delete_address.error: {e}'