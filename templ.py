from flask import Flask, request, render_template

app = Flask(__name__)

# Главная страница. Обрабатывает GET и POST запросы.
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем имя пользователя из формы
        name = request.form["username"]
        return f"Привет, {name}!"  # Возвращаем приветствие
    # Отправляем HTML-шаблон
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
