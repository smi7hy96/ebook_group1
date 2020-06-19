from flask import Flask, render_template, request
from database.ebooks_table import *
from database.booking_table import *
from database.users_table import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new-book")
def all_book():
    return render_template("new-book.html")

@app.route("/book_template/<int:id>")
def book_template(id):
    # book = DBEBooks()
    # result = book.select_one_book(id)  # will retrieve different data depending on id
    ## example query
    result_ex = [1, "Homo Deus", "Yuval Noah Harari", "Non-Fiction", "2015", "https://images-na.ssl-images-amazon.com/images/I/71FX96Ae-PL.jpg", "Sapiens showed us where we came from. Homo Deus shows us where we're going. War is obsolete. You are more likely to commit suicide than be killed in conflict. Famine is disappearing. You are at more risk of obesity than starvation. Death is just a technical problem. Equality is out - but immortality is in. What does our future hold? Yuval Noah Harari, author of the bestselling phenomenon Sapiens envisions a not-too-distant world in which we face a new set of challenges. Homo Deus explores the projects, dreams and nightmares that will shape the twenty-first century - from overcoming death to creating artificial life. It asks the fundamental questions: Where do we go from here? And how will we protect this fragile world from our own destructive powers? 'Homo Deus will shock you. It will entertain you. Above all, it will make you think in ways you had not thought before'. (Daniel Kahneman, author of Thinking Fast, and Slow)."]  # hard-coded can remove once db active
    title = result_ex[1]
    author = result_ex[2]
    genre = result_ex[3]
    release_date = result_ex[4]
    image_source = result_ex[5]
    description = result_ex[6]
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
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
