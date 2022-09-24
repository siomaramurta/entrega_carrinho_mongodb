
async def create_address(address_collection, address):
    try:
        info_insert_address = await address_collection.insert_one(address)
        if info_insert_address:
            return info_insert_address
    except Exception as e:
        print(f'get_addresses.error: {e}')

async def get_addresses(address_collection, user_id):
    try:
        data = await address_collection.find_one({'_id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_addresses.error: {e}') 
    
    """ 
    
    ● Pesquisar pelos endereços de um usuário.
    ● Remover um endereço do usuário pelo seu código identificador.
    
    try:
        data = await users_collection.update_one(
            {'_id': user_id},
            {'address': {address}})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')
            
            if address.inserted_id:
                address = await get_address(address_collection, address.inserted_id)
                return address

    except Exception as e:
            print(f'create_address.error: {e}')

async def get_address(address_collection, user_id):
    try:
        data = await address_collection.find_one({'_id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}') """
    

