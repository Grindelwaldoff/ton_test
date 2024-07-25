from python:3.12-slim

workdir /app

copy . .

run pip install -r requirements.txt --no-cache-dir