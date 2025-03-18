from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":  # если пользователь вводит свое имя, то делаем что-то
        name = request.form["username"]  # возьмем текст из формы который он отправил
        return f"Привет {name}!"

        # при GET запросе выполнится эта часть, вернем html форму для ввода
    return """
            <form action="/" method="post">
                <p>
    	            <label for="username">Username</label>
    	            <input type="text" name="username">
    	        </p>
    	    	<p>
    	            <input type="submit" value="Отправить" />
    	        </p>
            </form>
            """


if __name__ == '__main__':
     app.run(debug=True)