import random
import string


def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_num_generator(size=5):
    return ''.join(random.choice(string.digits) for _ in range(size))