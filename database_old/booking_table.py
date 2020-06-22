from database_old.db_connect import DBConnect


class DBBooking(DBConnect):
    def __init__(self):
        super().__init__()

    def insert_booking(self, user_id, book_id, date):
        ins = self.booking.insert().values(user_id=user_id, book_id=book_id, date=date)
        result = self.conn.execute(ins)
        return result.inserted_primary_key



