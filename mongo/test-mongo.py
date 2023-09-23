from dbconfig import DbConnection
from dbconfig import UsersDao


user_dao = UsersDao()

test_user = {
    'id': -2,
    'username': 'urmom2',
    'pass': 'urmomagain2',
}
user_dao.insert(test_user)