'''
We have the following dictionary containing user details:

user = {
    'user_name': 'my_user',
    'password': 'password',
    'email': 'my_email@example.com',
    'address': '123 Main Street, New York, 98109',
    'country': 'US'
}

Delete the sensitive information from the dictionary present in the list of
sensitive_info = ['password', 'address']
'''

user = {
    'user_name': 'my_user',
    'password': 'password',
    'email': 'my_email@example.com',
    'address': '123 Main Street, New York, 98109',
    'country': 'US'
}
sensitive_info = ['password', 'address', "phone"]
for info in sensitive_info:
    if info in user:
        print(f'Deleted => Key is: {info} and value is: {user[info]}')
        user.pop(info)
    else:
        print(f'{info} is not present in the user')
print(user)