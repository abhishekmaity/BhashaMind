# backend-python/app/queue/consumer.py

import json
from app.classifier import classify_text  # or summarizer.py as needed
from app.queue.connection import get_connection

async def start_consumer(queue_name: str):
    conn = await get_connection()
    channel = await conn.channel()
    queue = await channel.declare_queue(queue_name, durable=True)

    async def on_message(message):
        async with message.process():
            payload = json.loads(message.body)
            print("📥 Received Task:", payload)
            text = payload["text"]
            task = payload.get("task")

            if task == "classify":
                result = await classify_text(text)
                print("✅ Classification:", result)

    await queue.consume(on_message)
