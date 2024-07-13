from session import Session
from db import cursor, conn, commit
from models import User
from utils import Response, hash_password, check_password
from prints import *

session = Session()


@commit
def login(username: str, password: str):
    user: User | None = session.check_session()
    if user:
        return Response('You already logged in', 404)
    get_user_by_username = '''
    select * from users where username = %s;
    '''
    cursor.execute(get_user_by_username, (username,))
    user_data = cursor.fetchone()
    if not user_data:
        return Response('User not found', 404)
    user = User(username=user_data[1], password=user_data[2], role=user_data[3],
                status=user_data[4], login_try_count=user_data[5])

    if password != user_data[2]:
        login_try_count_query = '''
        select login_try_count from users where id = %s;
        '''
        my_id = user_data[0]
        cursor.execute(login_try_count_query, (my_id,))
        login_try_count_data = cursor.fetchone()
        if login_try_count_data[0] >= 3:
            return Response('You are blocked', 404)
        update_user_query = '''
        update users set login_try_count = login_try_count + 1 where username = %s;
        '''
        cursor.execute(update_user_query, (username,))
        return Response('Wrong Password', 404)
    session.add_session(user)
    return Response('User successfully logged in', 200)


def login_check():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = login(username, password)
    if response.status_code == 200:
        print_success('True')
        print_success(response.data)

    else:
        print_fail('False')
        print_fail(response.data)


@commit
def register_user():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    role = input('Enter your role: ')
    status = input('Enter your status: ')
    data = (username, password, role, status, 0)
    insert_user_query = '''
        insert into users (username, password, role, status, login_try_count)
        values (%s, %s, %s, %s, %s);
    '''
    cursor.execute(insert_user_query, data)
    print_success('You are registered successfully')


