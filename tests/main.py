from login import *
from user import *
from bpla import *
from flight import *
base_url = "http://192.168.32.142:9898"

print(post_login(login))
print(post_user(user))
print(post_bpla(bpla))
print(post_flight(flight))


