from flask import abort, redirect, url_for, Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    if user.authenticated(): # если пользователь авторизован направляем его на маршрут home
        return redirect(url_for("home"))
    return redirect(url_for('login')) # перенаправляем на маршрут login

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/login') # простой маршрут для входа
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
    return render_template("login.html")

if __name__ == '__main__':
     app.run(debug=True)