from sqlalchemy import *
from database.db_connect import DBConnect


class DBEBooks(DBConnect):
    def __init__(self):
        super().__init__()

    def insert_ebook(self, title, genre, release_date, user_id):
        ins = self.ebooks.insert().values(title=title, genre=genre, release_date=release_date, user_id=user_id)
        result = self.conn.execute(ins)
        return result.inserted_primary_key


