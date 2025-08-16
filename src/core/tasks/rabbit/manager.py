"""RabbitMQ manager module."""

# -- Imports

import asyncio
from aio_pika import connect_robust, RobustConnection, RobustChannel, Message
from contextlib import asynccontextmanager
from typing import Callable

# --


class RabbitMQManager:

    def __init__(self, url: str = "amqp://guest:guest@localhost/"):
        self.url = url
        self.connection: RobustConnection | None = None
        self.channel: RobustChannel | None = None

    async def connect(self):
        self.connection = await connect_robust(self.url)
        self.channel = await self.connection.channel()

    async def publish(self, queue_name: str, message: str):
        await self.channel.default_exchange.publish(
            Message(body=message.encode()),
            routing_key=queue_name,
        )

    async def consume(self, queue_name: str, callback: Callable):
        queue = await self.channel.declare_queue(queue_name)
        await queue.consume(callback)

    async def close(self):
        if self.channel:
            await self.channel.close()
        if self.connection:
            await self.connection.close()


@asynccontextmanager
async def get_rabbitmq_manager():
    manager = RabbitMQManager()
    await manager.connect()
    try:
        yield manager
    finally:
        await manager.close()


async def process_message(message):
    print(f"Get message: {message.body.decode()}")
    await message.ack()


async def main():
    async with get_rabbitmq_manager() as manager:

        asyncio.create_task(
            manager.consume(
                queue_name="messages",
                callback=process_message,
            ),
        )

        await manager.publish("messages", "Hello RabbitMQ!")
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
