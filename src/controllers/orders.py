from src.server.database import db
from src.server.database import connect_db, db, disconnect_db
from datetime import datetime

from src.models.order import (
    create_order,
    delete_order
)

async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    orders_collection = db.orders_collection

    order = {
                "user": {
                    "email": "ludomagalu@gmail.com",
                    "password": "213sd312re3",
                    "is_active": True,
                    "is_admin": False
                },
                "price": 0.0,
                "paid": True,
                "create": str(datetime.now()),
                "address": {
                    "street": "Rua III, 342",
                    "cep": "31800555",
                    "district": "Ponta Negra",
                    "city": "Belo Horizonte",
                    "state": "Minas Gerais",
                    "is_delivery": True
                    },
                "authority": order.authority
            }
    if option == '12':
        order = await create_order(
            orders_collection,
            order
        )
        print(order)
    elif option == '13':
        order = await delete_order(
            orders_collection,
            id
        )
        result = await delete_order(
            orders_collection,
            id
        )
        print(result)  

    await disconnect_db()