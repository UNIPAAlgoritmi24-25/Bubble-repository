from random import randint


def random_list(size, start=0, stop=100):
    """Provides a list containing randomly generated values."""
    return [randint(start, stop) for _ in range(size)]