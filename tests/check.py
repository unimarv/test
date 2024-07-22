import subprocess
import time

def get_token():
    # Запустить другую программу, чтобы получить токен
    result = subprocess.run(['python', 'login.py'], stdout=subprocess.PIPE)
    token = result.stdout.decode().strip()
    return token

class TokenProvider:
    def __init__(self):
        self.token = None
        self.token_expiration = 0  # время истечения токена в секундах

    def get_token(self):
        if self.token is None or time.time() > self.token_expiration:
            # Токен истек или не существует, запустить другую программу и получить токен
            self.token = get_token()
            self.token_expiration = time.time() + 3600  # кэшировать токен на 1 час
        return self.token

token_provider = TokenProvider()

# Использовать токен
print(token_provider.get_token())  # Запустит login.py и получит токен
print(token_provider.get_token())  # Опять запустит login.py и получит токен
print(token_provider.get_token())  # И снова запустит login.py и получит токен