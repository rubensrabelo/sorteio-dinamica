from utils import random_times
from utils import secure_shuffle
from data import themes


def draw_themes():
    times = random_times()
    last_result = None

    for _ in range(times):
        last_result = secure_shuffle(themes)

    return last_result, times
