from .secure_choice import secure_choice

def run_multiple_times(items, times):
    last = None
    for _ in range(times):
        last = secure_choice(items)
    return last
