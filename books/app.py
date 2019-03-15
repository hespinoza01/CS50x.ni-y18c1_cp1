from flask import Flask, render_template as render
from config import Config
from models import db, Category, Book

app = Flask(__name__, static_folder="public", template_folder="views")

app.config.from_object(Config)


@app.route('/')
def index():
    books = Book.query.all()
    categories = Category.query.all()
    return render("index.html", books=books, categories=categories)


@app.route('/book')
def book():
    return render("book.html")


@app.route('/category')
def category():
    return render("category.html")


if __name__ == "__main__":
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=8000)

