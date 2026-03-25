import random
import string
import time

DIGITS = string.digits
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
SPECIAL = "#[]().,!@&^%*"


def generate_password():
    length = random.randint(8, 16)

    all_chars = DIGITS + LOWER + UPPER + SPECIAL

    required = [
        random.choice(DIGITS),
        random.choice(LOWER),
        random.choice(UPPER),
        random.choice(SPECIAL),
    ]

    rest = random.choices(all_chars, k=length - len(required))
    chars = required + rest
    random.shuffle(chars)

    return "".join(chars).encode("utf-8")

def application(environ, start_response):
    password = generate_password()
    
    time.sleep(0.05)

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ("Content-Length", str(len(password))),
    ]

    start_response(status, headers)
    return [password]