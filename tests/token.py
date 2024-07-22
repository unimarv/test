import login
from classes import Login

response = login.post_login(Login('cats', 'a'))
token = response[1]['token']
print(f"token={token}")
