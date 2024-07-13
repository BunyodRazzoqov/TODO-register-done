import bcrypt


class Response:
    def __init__(self, data: str, status_code: int):
        self.data = data
        self.status_code = status_code


def hash_password(raw_password):
    raw_password = b'hello'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=raw_password, salt=salt)
    return hashed


def check_password(user_password, hashed):
    user_password = b'hello'
    check = bcrypt.checkpw(
        password=user_password,
        hashed_password=hashed
    )
    if check:
        return True
    return False


# my_password = hash_password('hello')
# a = check_password('hello', my_password)
# print(a)


def match_password(raw_password, encoded_password):
    encoded_password = b'encoded_password'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(encoded_password, salt)
    # if hashed == hash_password():
