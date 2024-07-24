import asyncio

from pytoniq import LiteClient, BlockIdExt

from db.models import AddressModel
from scanner.block_scanner import BlockScanner

from contract_data_worker import address_task


async def handle_block(block: BlockIdExt):
    if block.workchain == -1:
        return
    transactions = await client.raw_get_block_transactions_ext(block)
    for transaction in transactions:
        # сохраняем их в бд, вместе со смарт контрактом и полем статус = 0
        dest = transaction.in_msg.info.dest
        src = transaction.in_msg.info.src
        print([dest, src])
        AddressModel.insert_address(dest) if dest else ...
        AddressModel.insert_address(src) if src else ...


client = LiteClient.from_mainnet_config(ls_i=0, trust_level=2, timeout=15)


async def fetch_blocks():
    await BlockScanner(client=client, block_handler=handle_block).run()


async def main():
    await client.connect()
    await client.reconnect()
    address_task.delay()
    block = await fetch_blocks()


if __name__ == "__main__":
    asyncio.run(main())
