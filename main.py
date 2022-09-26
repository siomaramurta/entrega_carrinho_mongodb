import asyncio

from src.controllers.users import users_crud
loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())

#----------------------------------------------------------------

#Para usar as demais chamadas, comentar a chamada acima e descomentar a chamada que será usada

from src.controllers.addresses import address_crud
loop = asyncio.get_event_loop()
loop.run_until_complete(address_crud())

from src.controllers.products import products_crud
loop = asyncio.get_event_loop()
loop.run_until_complete(products_crud())

from src.controllers.orders import orders_crud
loop = asyncio.get_event_loop()
loop.run_until_complete(orders_crud())

from src.controllers.order_items import cart_crud
loop = asyncio.get_event_loop()
loop.run_until_complete(cart_crud())