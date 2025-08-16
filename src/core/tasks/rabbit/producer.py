from pika import BlockingConnection, ConnectionParameters

connection_params = ConnectionParameters(
    host="localhost",
    port=5672,
)


def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue="messages")

            ch.basic_publish(
                exchange="",
                routing_key="messages",
                body="Hello gogi",
            )
            print("Message sent")


if __name__ == "__main__":
    main()
