from sqlalchemy import *
from database.db_connect import DBConnect


class DBEBooks(DBConnect):
    def __init__(self):
        super().__init__()

    def insert_ebook(self, title, author, genre, release_date, image_source, description, user_id=None):
        if user_id is None:
            user_id = 1
        ins = self.ebooks.insert().values(title=title, author=author, genre=genre, release_date=release_date, image_source=image_source, description=description, user_id=user_id)
        print(str(ins))
        result = self.conn.execute(ins)
        return result.inserted_primary_key

    def select_all_books(self):
        s = select([self.ebooks])
        result_list = []
        result = self.conn.execute(s)
        while True:
            row = result.fetchone()
            if row is None:
                break
            result_list.append(row)
        title_list = []
        author_list = []
        genre_list = []
        release_date_list = []
        image_source_list = []
        description_list = []
        return_list = []
        for value in result_list:
            title_list.append(value[1])
            author_list.append(value[2])
            genre_list.append(value[3])
            release_date_list.append(value[4])
            image_source_list.append(value[5])
            description_list.append(value[6])

        return_list.append(title_list)
        return_list.append(author_list)
        return_list.append(genre_list)
        return_list.append(release_date_list)
        return_list.append(image_source_list)
        return_list.append(description_list)
        return return_list

    def select_books_by_genre(self, genre):
        result_list = []
        s = select([self.ebooks]).\
            where(and_(self.ebooks.c.genre == genre))
        result = self.conn.execute(s)
        while True:
            row = result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def select_books_by_name(self, name):
        result_list = []
        s = select([self.ebooks]).\
            where(and_(self.ebooks.c.title.like(name)))
        result = self.conn.execute(s)
        while True:
            row = result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def select_one_book(self, book_id):
        result_list = []
        s = select([self.ebooks]).\
            where(and_(self.ebooks.c.book_id == book_id))
        result = self.conn.execute(s)
        while True:
            row = result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list
