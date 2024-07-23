import time

import requests
from peewee import OperationalError
from celery import Celery

from db.models import AddressModel, database


celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

ton_api = "https://toncenter.com/api/v3/account?address={address}"


@celery_app.task
def address_task():
    database.connect()
    while True:
        try:
            addresses: AddressModel = AddressModel.filter(status=0)
            for address in addresses:
                time.sleep(1)
                response = requests.get(
                    ton_api.format(address=address.wallet_address)
                )
                data = response.json()
                print(data)
                if data.get("code") and data.get("data"):
                    address.code = response.json().get("code")
                    address.data = response.json().get("data")
                address.status = True
                address.update_dt = time.time()
                address.save()
        except OperationalError:
            continue
