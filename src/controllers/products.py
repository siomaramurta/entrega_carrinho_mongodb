from src.server.database import db

from src.models.product import (
    create_product,
    get_product,
    delete_product
)

from src.server.database import connect_db, db, disconnect_db

async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    products_collection = db.products_collection

    product =  {
        "name": "Sorvete",
        "description": "Pote de Sorvete Eskimó 2 Litros - Delicioso sorvete napolitano ( chocolate, creme e morango)",
        "price": 9.99,
        "image": "https://www.magazineluiza.com.br/pote-de-sorvete-eskimo-2-litros-eskimo-sorvetes/p/jf5e417kg7/me/svte/",
        "code": "123"
    }

    if option == '10':
        # create product
        product = await create_product(
            products_collection,
            product
        )
        print(product)
    
    elif option == '11':
        # delete
        product = await get_product(
            products_collection,
            product["code"]
        )

        result = await delete_product(
            products_collection,
            product["code"]
        )

        print(result)
    
    await disconnect_db()