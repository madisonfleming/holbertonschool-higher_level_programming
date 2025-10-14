#!/usr/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)
# remove data set for the checker
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_data():
    # user = users.get(username)
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def get_status():
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    output = users[username]
    output["username"] = username
    return jsonify(output)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # if username in users:
        # return jsonify({"error": "User already exists"}), 400

    users[username] = data

    return jsonify({
        "message": "User created",
        "user": data
     }), 201


if __name__ == "__main__":
    app.run()
