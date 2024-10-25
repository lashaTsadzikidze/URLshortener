import string
import random

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))