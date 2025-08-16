from pika import BlockingConnection, ConnectionParameters

connection_params = ConnectionParameters(
    host="localhost",
    port=5672,
)


def process_message(ch, method, properties, body: bytes):
    print(f"Get message: {body.decode()}")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue="messages")

            ch.basic_consume(
                queue="messages",
                on_message_callback=process_message,
                # auto_ack=True,
            )
            print("Waiting messages ...")
            ch.start_consuming()


if __name__ == "__main__":
    main()
