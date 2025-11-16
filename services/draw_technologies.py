from utils import random_times, run_multiple_times
from data import back
from data import front
from data import mobile


def draw_technologies():
    repetitions = random_times()
    result = {
        "backend": run_multiple_times(back, repetitions),
        "frontend": run_multiple_times(front, repetitions),
        "mobile": run_multiple_times(mobile, repetitions),
    }

    return repetitions, result
