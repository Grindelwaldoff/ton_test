import json
import asyncio

from db.models import AddressModel


async def data_unload():
    # выгрузка данных в json
    with open('./unload.json', 'w') as file:
        return json.dump([*AddressModel.unload()], file, indent=4)


if __name__ == '__main__':
    asyncio.run(data_unload())
