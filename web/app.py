from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId

sample = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
mydb = client["ipa2025"]
mycol = mydb["routers"]


@sample.route("/")
def main():
    routers = mycol.find()
    return render_template("index.html", data=routers)

@sample.route("/add", methods=["POST"])
def add_comment():
    ip_address = request.form.get("ip_address")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip_address and username and password:
        data = { "ip_address": ip_address, "username": username, "password": password }
        mycol.insert_one(data)
    return redirect(url_for("main"))

@sample.route("/delete", methods=["POST"])
def delete_comment():
    try:
        router_id = request.form.get("_id")
        if router_id:
            mycol.delete_one({ '_id': ObjectId(router_id)})
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)