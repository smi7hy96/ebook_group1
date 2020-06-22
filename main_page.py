from flask import Flask, render_template, request
from database.database_full_connection import *
from database.example_books import *
app = Flask(__name__)


@app.route("/")
def home():
    result_list = select_six_random()
    titles = result_list[0]
    authors = result_list[1]
    genres = result_list[2]
    release_dates = result_list[3]
    image_sources = result_list[4]
    descriptions = result_list[5]
    book_ids = result_list[6]
    return render_template("flip_card.html", titles=titles, authors=authors, genres=genres, release_dates=release_dates,
                           image_sources=image_sources, descriptions=descriptions, book_ids=book_ids)

@app.route("/all-books")
def all_books():
    result_list = select_all_separate()
    titles = result_list[0]
    authors = result_list[1]
    genres = result_list[2]
    release_dates = result_list[3]
    image_sources = result_list[4]
    descriptions = result_list[5]
    book_ids = result_list[6]
    return render_template("all_books.html", titles=titles, authors=authors, genres=genres, release_dates=release_dates, image_sources=image_sources, descriptions=descriptions, book_ids=book_ids)


@app.route("/book_id/<int:id>")
def book_id(id):
    new_list = []
    result_list = select_one_book(id)  # will retrieve different data depending on id
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


@app.route("/search_book")
def search_book():
    query = request.args['search']
    result_list = get_by_name(query)
    titles = result_list[0]
    authors = result_list[1]
    genres = result_list[2]
    release_dates = result_list[3]
    image_sources = result_list[4]
    descriptions = result_list[5]
    return render_template("search_book.html", titles=titles, authors=authors, genres=genres, release_dates=release_dates,
                           image_sources=image_sources, descriptions=descriptions, query=query)


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


# Add new book page methods - untested until page templates created.
@app.route("/add_book")
def add_book():
    return render_template("add_book.html")

@app.route("/add_new_book")
def add_new_book():
    title = request.args['title']
    author = request.args['author']
    genre = request.args['genre']
    release_date = request.args['release_date']
    image_source = request.args['image_source']
    description = request.args['description']
    return_num = insert_ebook(title, author, genre, release_date, image_source, description)
    return str(return_num[0])


if __name__ == "__main__":
    app.run(debug=True)
