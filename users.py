from flask import Flask

app = Flask(__name__)

# Пример базы данных
users = {
    1: {"name": "Алексей", "city": "Москва", "age": 32},
    2: {"name": "Мария", "city": "Санкт-Петербург", "age": 18},
    3: {"name": "Иван", "city": "Новосибирск", "age": 20}
}

@app.route("/users/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id, False)
    if user:
        # Если пользователь найден, возвращаем его данные
        return f"""
        <h1>Профиль пользователя</h1>
        <p>Имя: {user['name']}</p>
        <p>Город: {user['city']}</p>
        <p>Возраст: {user['age']}</p>
        """
    else:
        # Если пользователь не найден
        return "Пользователь не найден"

if __name__ == "__main__":
    app.run(debug=True)