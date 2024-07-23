# ton_test


## Запуск
сначало запускаем селери (не забыва запустить сервер редис)
```
celery -A contract_data_worker worker --loglevel=info
```

теперь непосредственно сам скрипт
```
python main.py
```

если какие-то проблемы с бд - ее можно пересоздать запусти отдельно models.py
```
python models.py
```