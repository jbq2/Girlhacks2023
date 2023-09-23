from dbconfig import DbConnection
from dbconfig import UsersDao


user_dao = UsersDao()

test_user = {
    'id': -2,
    'username': 'urmom2',
    'pass': 'urmomagain2',
}

print(user_dao.find_any({}))