from sqlalchemy import *


class DBConnect:
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        self.metadata = MetaData()
        self.conn = self.engine.connect()
        self.users = None
        self.ebooks = None
        self.booking = None

    def create_all_tables(self):
        users = Table('users', self.metadata,
                      Column('user_id', Integer, primary_key=True),
                      Column('name', String(20)),
                      Column('email', String(30)),
                      Column('phone_no', String(15)),
                      )
        self.users = users
        ebooks = Table('ebooks', self.metadata,
                       Column('book_id', Integer, primary_key=True),
                       Column('title', String),
                       Column('author', String),
                       Column('genre', String),
                       Column('release_date', String),
                       Column('image_source', String),
                       Column('description', String),
                       Column('user_id', None, ForeignKey('users.user_id'))
                       )
        self.ebooks = ebooks
        booking = Table('booking', self.metadata,
                        Column('booking_id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.user_id')),
                        Column('book_id', None, ForeignKey('ebooks.book_id')),
                        Column('date', String)
                        )
        self.booking = booking
        self.metadata.create_all(engine)
