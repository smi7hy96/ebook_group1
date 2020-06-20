from flask import Flask, render_template, request
from database.ebooks_table import *
from database.booking_table import *
from database.users_table import *
from database.user_example import *
from database.example_books import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("flip_card.html")

@app.route("/new-book")
def all_book():
    return render_template("new-book.html")


@app.route("/book_template/<int:id>")
def book_template(id):
    book = DBEBooks()
    book.create_all_tables()
    example_book(book)
    new_list = []
    result_list = book.select_one_book(id)  # will retrieve different data depending on id
    ## example query
    for result in result_list:
        for value in result:
            new_list.append(value)

    title = new_list[1]
    author = new_list[2]
    genre = new_list[3]
    release_date = new_list[4]
    image_source = new_list[5]
    description = new_list[6]
    return render_template("book_template.html", title=title, author=author, genre=genre, release_date=release_date, image_source=image_source, description=description)


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
#     description = request.form['description']
#     release_date = request.form['release_date']
#     image_source = request.form['image_source']
#     book = DBEBooks()
#     book.insert_ebook(title, author, genre, release_date, image_source, description)
#     return render_template("index_probs_delete.html")


if __name__ == "__main__":
    app.run(debug=True)
