from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

if __name__ == "__main__":
    app.run(debug = True, port=8080)