from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    technologies = [
        ["Python", "Язык программирования", 1991, 1],
        ["Flask", "Веб-фреймворк на Python", 2010, 2],
        ["VS Code", "Редактор кода", 2015, 3],
        ["Docker", "Контейнеризация приложений", 2013, 4],
        ["Git", "Система контроля версий", 2005, 5]
    ]
    return render_template("index.html", technologies=technologies)


