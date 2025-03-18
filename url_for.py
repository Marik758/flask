from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    print(url_for('login'))  # Генерация URL для функции login
    return "Hello, world!"

@app.route("/login2")
def login():
    return "Login page"


if __name__ == '__main__':
     app.run(debug=True)