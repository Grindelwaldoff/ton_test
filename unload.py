import json
import asyncio

from db.models import AddressModel


async def data_unload():
    # выгрузка данных в json
    addresses = AddressModel.unload()
    result = []
    for address in addresses:
        result.append(address)
    return json.dumps(result)


if __name__ == '__main__':
    asyncio.run(data_unload())
