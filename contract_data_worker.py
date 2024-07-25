import time

import requests
from peewee import OperationalError
from celery import Celery

from db.models import AddressModel, database


celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

ton_api = "https://toncenter.com/api/v3/account?address={address}"


@celery_app.task
def address_task():
    database.connect()
    while True:
        try:
            for address in AddressModel.filter(status=0):
                time.sleep(1)
                response = requests.get(
                    ton_api.format(address=address.wallet_address)
                )
                data = response.json()
                print(data)
                if data.get("code") and data.get("data"):
                    address.code = data.get("code")
                    address.data = data.get("data")
                address.status = True
                address.update_dt = time.time()
                address.save()
        except OperationalError:
            continue
