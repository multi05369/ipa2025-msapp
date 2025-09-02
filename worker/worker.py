import pika, json, dotenv, os, database, time
import connection as conn
from pymongo import MongoClient

dotenv.load_dotenv()

def save_interface_status(ip, output):
    database.set_router_info({
        "ip_address": ip,
        "time": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
        "output": output
    })

def main():
    def callback(ch, method, properties, body):
        try:
            data = json.loads(body)
            print("Decoded JSON:", data)
            ip = data.get("ip_address")
            username = data.get("username")
            password = data.get("password")
            net_connect = conn.connection(ip, username, password)
            output = net_connect.send_command("show ip int brief", use_textfsm=True)
            print(f"Output from {ip}:\n{output}")
            net_connect.disconnect()
            # Save to MongoDB
            save_interface_status(ip, output)
            print(f"Saved output for {ip} to MongoDB.")
        except Exception as e:
            print("Failed to process message:", e)

    credentials = pika.PlainCredentials(
        os.getenv("RABBITMQ_USER"),
        os.getenv("RABBITMQ_PASSWORD")
    )
    for i in range(10):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials)
            )
            break
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not ready, retrying in 5 seconds...")
            time.sleep(5)
    else:
        print("Failed to connect to RabbitMQ after several attempts.")
        exit(1)
    channel = connection.channel()
    channel.queue_declare(queue='router_jobs')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='router_jobs', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()