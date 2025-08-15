from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400

    users[username] = {"username": username, "email": email}
    return jsonify({"message": "User added"}), 201

# PUT to update a user
@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    users[username]['email'] = email
    return jsonify({"message": "User updated"}), 200

# DELETE a user
@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username in users:
        del users[username]
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

