def check_username(username):
    if len(username) >= 5:
        return 'valid username'
    else:
        return 'invalid username'
def check_password(password):
    has_number=False
    has_uppercase=False
    for char in password:
        if char.isdigit():
            has_number=True
        if char.isupper():
            has_uppercase=True
    if len(password) >= 8 and has_number and has_uppercase:
        return 'strong password'
    else:
        return 'password too weak'

username=input('Enter your username:')
password=input('Enter your password: ')
username_result = check_username(username)
password_result = check_password(password)

print(username_result)
print(password_result)