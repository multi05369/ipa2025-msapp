import pika


def produce(host, user, passwd, body):
    credentials = pika.PlainCredentials(user, passwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host,
        credentials=credentials))

    channel = connection.channel()

    channel.exchange_declare(
        exchange="jobs",
        exchange_type="direct")

    channel.queue_declare(queue="router_jobs")
    channel.queue_bind(queue="router_jobs", exchange="jobs", routing_key="check_interfaces")

    channel.basic_publish(exchange="jobs", routing_key="check_interfaces", body=body)

    connection.close()


if __name__ == "__main__":
    produce("rabbitmq", "user", "pass", "192.168.1.44")
