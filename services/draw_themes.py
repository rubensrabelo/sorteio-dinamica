import importlib

from utils import random_times
from utils import secure_shuffle
import data.themes as themes_module


def draw_themes():
    importlib.reload(themes_module)
    times = random_times()
    last_result = None

    for _ in range(times):
        last_result = secure_shuffle(themes_module.themes)

    return last_result, times
