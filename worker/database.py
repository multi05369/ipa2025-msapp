import os
from pymongo import MongoClient


def set_router_info(router_info):
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["ipa2025"]
    collection = db["interface_status"]

    collection.insert_one(router_info)
    print(f"Inserted new document for {router_info['ip_address']}.")

    client.close()
