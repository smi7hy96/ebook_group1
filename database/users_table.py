from sqlalchemy import *
from database.db_connect import DBConnect


class DBUsers(DBConnect):
    def __init__(self):
        super().__init__()

    def insert_user(self, name, email, phone_no):
        self.create_all_tables()
        ins = self.users.insert().values(name=name, email=email, phone_no=phone_no)
        print(str(ins))
        result = self.conn.execute(ins)
        return result.inserted_primary_key


