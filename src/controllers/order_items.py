from src.server.database import db
from datetime import datetime

from src.models.order_item import (
    get_order_item,
    insert_product_cart,
    get_order_item_sum,
    get_order_items_by_id
)
from src.server.database import connect_db, db, disconnect_db

async def cart_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_items_collection = db.order_items_collection
    products_collection = db.products_collection
    orders_collection = db.orders_collection

    order_item = {
        "order": {
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
            },
        "product": {
            "name": "Sorvete",
            "description": "Pote de Sorvete Eskimó 2 Litros - Delicioso sorvete napolitano ( chocolate, creme e morango)",
            "price": 9.99,
            "image": "https://www.magazineluiza.com.br/pote-de-sorvete-eskimo-2-litros-eskimo-sorvetes/p/jf5e417kg7/me/svte/",
            "code": "123"
        }
    }

    if option == '14':
        order_item = await insert_product_cart(
            orders_collection,
            products_collection,
            order_items_collection
        )
        print(order_item)

    elif option == '15':
        cart_sum = await get_order_item_sum(
            order_items_collection, 
            id
            )
        print(cart_sum)
    