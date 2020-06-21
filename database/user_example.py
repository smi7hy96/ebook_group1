from database.users_table import *


def example_user(user_new):
    user_new.insert_user("Ryan", "ryan@example.com", "0715621616", "ryan1")
    user_new.insert_user("Mergim", "mergim@example.com", "114165468541", "mergim1")
    user_new.insert_user("Patrick", "patrick@example.com", "17847847", "patrick1")
    user_new.insert_user("Avraj", "avraj@example.com", "0798452315", "avraj1")


user = DBUsers()
user.create_all_tables()
example_user(user)
print(user.log_in(1, "ryan1"))