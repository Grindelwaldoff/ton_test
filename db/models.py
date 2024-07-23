from pytoniq import Address
from peewee import (
    Model,
    CharField,
    BooleanField,
    SqliteDatabase,
    BigIntegerField,
)


database = SqliteDatabase("blockchain.db", pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})


class AddressModel(Model):
    """Модель для хранения адресов."""

    wallet_address = CharField()
    smart_contract = CharField()
    status = BooleanField(default=False)
    update_dt = BigIntegerField(null=True)
    code = CharField(null=True)
    data = CharField(null=True)

    @staticmethod
    def insert_address(address: Address):
        try:
            print(address)
            return AddressModel.create(
                wallet_address=address.to_str(),
                smart_contract=address.to_str(is_user_friendly=False),
            )
        except AttributeError:
            ...

    class Meta:
        database = database


def init_db(db: SqliteDatabase, tables: list):
    """Метод инициализирующий бд."""
    db.connect()
    db.drop_tables(tables)
    db.create_tables(tables)


if __name__ == "__main__":
    init_db(database, [AddressModel])
