from dbconfig import DbConnection
from dbconfig import UsersDao


user_dao = UsersDao()

print(user_dao.insert_one({
    'username': 'urmom'
}))