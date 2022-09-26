from src.server.database import db

from src.models.address import (
    create_address,
    get_addresses,
    delete_address
)

from src.server.database import connect_db, db, disconnect_db

async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    address_collection = db.address_collection

    address =  {
       "user": {
            "_id" : 'ObjectId("6329262e79bd12f9b190b66f")',
            "email" : "lu_domagalu@gmail.com",
            "password" : "213sd312re3",
            "is_active" : True,
            "is_admin" : False
},
       "address": [
           {
            "street": "Rua III, 342",
            "cep": "31800555",
            "district": "Ponta Negra",
            "city": "Belo Horizonte",
            "state": "Minas Gerais",
            "is_delivery": True
            }
       ]
    }

    if option == '7':
        # create address
        address = await create_address(
            address_collection,
            address
        )
        print(address)

    elif option == '8':
        # get addresses
        address = await get_addresses(
            address_collection,
            id
        )
        
    elif option == '9':
        # delete
        address = await delete_address(
            address_collection,
            id
        )

        result = await delete_address(
            address_collection,
            id
        )
        print(result)    
        
    await disconnect_db()
