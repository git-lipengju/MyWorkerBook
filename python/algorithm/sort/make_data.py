import random


def get_range_data(count, start, end):
    data = random.sample(range(start, end), count)
    return data


def get_data(count):
    data = random.sample(range(1, count * 10), count)
    return data






