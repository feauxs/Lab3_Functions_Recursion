# Exercise 3: Intelligent Equipment Monitoring Pipeline
# Module: telemetry_module.py
# Generates the telemetry stream (used as a generator).

import random

LASTNAME = "CAMPOS"
SEEDNUM = 7
FAVORITEARTIST = "CAR SEAT HEADREST"


def telemetry_stream(count=15):
    """Generator that yields one reading at a time (some deliberately bad)."""
    seed = sum(ord(c) for c in LASTNAME + FAVORITEARTIST) * SEEDNUM
    random.seed(seed)

    for i in range(count):
        if i % 5 == 4:
            yield "ERR"            # bad reading on purpose
        else:
            yield round(random.uniform(-10, 180), 2)
