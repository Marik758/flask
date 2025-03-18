from flask import session, redirect, url_for, Flask, request, abort
import datetime
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex()
app.permanent_session_lifetime = datetime.timedelta(days=10)

@app.route('/')
def index():
    if 'username' in session: # ищем ключ username
        return f"""
        Logged in as {session["username"]}
        <br>
        <a href="/logout">Logout</a>
            """
    abort(401)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session.permanent = True
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <label>Name:
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # удалить имя пользователя из сеанса, если оно там есть
    session.pop('username', None)
    return redirect(url_for('index'))

@app.errorhandler(401)
def error401(e):
    return """
            <h2>You are not logged in<h2>
            <a href="/login">Login</a>
            """