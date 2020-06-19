from sqlalchemy import *
from database.db_connect import DBConnect


class DBEBooks(DBConnect):
    def __init__(self):
        super().__init__()

    def insert_ebook(self, title, author, genre, release_date, image_source, user_id=None):
        if user_id is None:
            user_id = 1
        ins = self.ebooks.insert().values(title=title, author=author, genre=genre, release_date=release_date, image_source=image_source, user_id=user_id)
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
        return result_list

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
