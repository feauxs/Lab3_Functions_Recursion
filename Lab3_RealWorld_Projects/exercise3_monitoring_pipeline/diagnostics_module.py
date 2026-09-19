# Exercise 3: Intelligent Equipment Monitoring Pipeline 
# Module: diagnostics_module.py
# Validates readings, flags abnormal ones, and analyzes them recursively.

# Lambda: flags a reading as abnormal 
is_abnormal = lambda value: value > 120 or value < 0

exercise_3_log = []

# Decorator: monitors the main processing function
def monitor(func):
    def wrapper(*args, **kwargs):
        exercise_3_log.append("[MONITOR] Starting stream processing...")
        result = func(*args, **kwargs)
        exercise_3_log.append("[MONITOR] Finished stream processing.")
        return result
    return wrapper

# Recursion: keeps reducing an abnormal value until it's back to normal
def reduce_abnormal(value, steps=0):
    if value <= 120:              # base condition
        return value, steps
    return reduce_abnormal(round(value * 0.8, 2), steps + 1)

@monitor
def process_stream(stream):
    valid = []
    invalid = []
    abnormal = []

    for reading in stream:
        try:
            value = float(reading)
        except ValueError:
            invalid.append(reading)
            continue

        valid.append(value)
        if is_abnormal(value):
            final_value, steps = reduce_abnormal(value)
            abnormal.append((value, steps, final_value))

    return valid, invalid, abnormal
