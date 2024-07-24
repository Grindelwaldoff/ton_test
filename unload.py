import json
import asyncio

from db.models import AddressModel


async def data_unload():
    # выгрузка данных в json
    addresses = AddressModel.unload()
    with open('./unload.json', 'w') as file:
        return json.dump([*addresses], file, indent=4)


if __name__ == '__main__':
    asyncio.run(data_unload())
