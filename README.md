[README (1).md](https://github.com/user-attachments/files/21801150/README.1.md)
# 📡 Flask User API

A simple **RESTful API** built with Flask to manage users in memory (no database).
Supports basic CRUD operations: **Create, Read, Update, Delete**.

## 📌 Features

* **GET** all users
* **POST** a new user
* **PUT** to update a user's email
* **DELETE** a user by username
* Uses in-memory storage (data is lost on restart)

## 🛠 Requirements

Install Python 3.x and the required dependency:

```bash
pip install flask
```

## 🚀 Running the API

1. Save the script as `app_api_flask.py`.
2. Run the Flask server:

   ```bash
   python app_api_flask.py
   ```
3. The API will be available at:

   ```
   http://127.0.0.1:5000
   ```

## ⚠️ Notes

* Data is stored **only in memory** — all users are lost when the server restarts.
* This API is meant for learning/demo purposes. Use a database for production.
