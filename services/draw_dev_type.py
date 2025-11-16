from utils import random_times
from utils import secure_shuffle
from data import dev_type


def draw_dev_type():
    times = random_times()
    last_result = None

    for _ in range(times):
        last_result = secure_shuffle(dev_type.dev_types)

    return last_result[0], times
