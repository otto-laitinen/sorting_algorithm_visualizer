import random


def generate_initial_list(n, min_value, max_value):
    lst = []

    for _ in range(n):
        value = random.randint(min_value, max_value)
        lst.append(value)

    return lst
