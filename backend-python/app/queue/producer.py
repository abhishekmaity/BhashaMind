# backend-python/app/queue/producer.py

import json
import aio_pika
from app.queue.connection import get_connection

async def send_task_to_queue(queue_name: str, payload: dict):
    conn = await get_connection()
    async with conn:
        channel = await conn.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(payload).encode()),
            routing_key=queue.name
        )
