# ton_test


## Запуск

```
cd docker # переходим в папку с файлом compose

docker compose up -d --build # запускаем сервисы

для получения выгрузки
docker ps # выводится список контейнеров

находим контейнер с параметрами python main.py - копируем его hash-id

docker exec -it <hash-id> bash # заходим в контейнер

python unload.py # выполняем данную команду внутри cli контейнера

cat unload.json # выводим получившийся результат

```

