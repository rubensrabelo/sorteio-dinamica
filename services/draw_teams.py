# services.py
from utils import random_times
from utils import secure_shuffle
from data import people


def draw_teams():
    times = random_times()
    final_order = people

    for _ in range(times):
        final_order = secure_shuffle(final_order)

    total = len(final_order)
    half = total // 2

    team1 = final_order[:half]
    team2 = final_order[half:]

    return times, team1, team2
