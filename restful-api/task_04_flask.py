#!/usr/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)
# remove data set for the checker
# users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def print_user(username):
    # user = users.get(username)
    return jsonify(username)


@app.route('/status', methods=['GET'])
def get_status():
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return {"error": "User not found"}


@app.route('/add_user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User created", "user": users[username]}), 201


if __name__ == "__main__": app.run()
