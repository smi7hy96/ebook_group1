from flask import Flask, render_template, request
from database.ebooks_table import *
from database.booking_table import *
from database.users_table import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book_template")
def book_template():
    return render_template("book_template.html")


@app.route("/book")
def book():
    return render_template("book.html")


# Add new book page methods - untested until page templates created.
# @app.route("/add_new_book")
# def add_new_book():
#     return render_template("add_new_book.html")
#
#
# @app.route("/add_new_book", methods=['POST'])
# def add_new_book_complete():
#     title = request.form['title']
#     author = request.form['author']
#     genre = request.form['genre']
#     release_date = request.form['release_date']
#     image_source = request.form['image_source']
#     book = DBEBooks()
#     book.insert_ebook(title, author, genre, release_date, image_source)
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
