from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://samuel:samuel123@localhost/collector'
database = SQLAlchemy(app)

class Data(database.Model):
    __tablename__ = "data"
    id = database.Column(database.INTEGER, primary_key=True)
    email = database.Column(database.String(120), unique=True)
    name = database.Column(database.String(120))
    country = database.Column(database.String(120))
    age = database.Column(database.INTEGER)

    def __init(self, email,name, country, age):
        self.email = email
        self.name = name
        self.country = country
        self.age = age


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email"]
        name = request.form["name"]
        age = request.form["age"]
        country = request.form["country"]

        return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run()