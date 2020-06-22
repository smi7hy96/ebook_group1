from sqlalchemy import *
from database_old.db_connect import DBConnect
from database.phsh import *


class DBUsers(DBConnect):
    def __init__(self):
        super().__init__()

    def insert_user(self, name, email, phone_no, password):
        hsh_pass = hash_password(password)
        ins = self.users.insert().values(name=name, email=email, phone_no=phone_no, password=hsh_pass)
        result = self.conn.execute(ins)
        return result.inserted_primary_key

    def log_in(self, user_id, password):
        result = self.select_one_user(user_id)
        if len(result) == 0:
            return False
        stored_pword = result[0][4]
        print(stored_pword)
        if verify_password(password, stored_pword):
            return True
        else:
            return False

    def select_one_user(self, user_id):
        result_list = []
        s = select([self.users]). \
            where(and_(self.users.c.user_id == user_id))
        result = self.conn.execute(s)
        while True:
            row = result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list


