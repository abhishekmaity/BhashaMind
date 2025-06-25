# backend-python/app/queue/connection.py

import aio_pika

RABBITMQ_URL = "amqp://user:pass@rabbitmq/"

async def get_connection():
    return await aio_pika.connect_robust(RABBITMQ_URL)
