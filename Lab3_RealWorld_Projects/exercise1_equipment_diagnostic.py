# Exercise 1: Equipment Diagnostic System

import random

# Student-specific inputs 
LASTNAME = "CAMPOS"
SEEDNUM = 7
FAVORITEARTIST = "CAR SEAT HEADREST"

execution_log = []

# Decorator: records every step that runs

def log_step(func):
    def wrapper(*args, **kwargs):
        execution_log.append(f"[LOG] Running {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

# Generate student-specific readings 
@log_step
def generate_readings():
    seed = sum(ord(c) for c in LASTNAME + FAVORITEARTIST) * SEEDNUM
    random.seed(seed)

    readings = []
    for i in range(10):
        value = round(random.uniform(20, 130), 2)
        if i == 3 or i == 7:        # force a couple of bad readings
            value = -value
        readings.append(value)
    readings.append("ERR")          # force one non-numeric reading
    return readings

# Validate one reading at a time 
@log_step
def validate_readings(readings):
    valid = []
    invalid = []
    for reading in readings:
        try:
            value = float(reading)
            if value < 0 or value > 150:
                raise ValueError("out of range")
            valid.append(value)
        except ValueError:
            invalid.append(reading)
    return valid, invalid

# Calculate the average
@log_step
def calculate_average(valid_readings):
    if len(valid_readings) == 0:
        return 0
    return round(sum(valid_readings) / len(valid_readings), 2)

# Classify the equipment condition
@log_step
def classify_condition(average):
    if average < 50:
        return "NORMAL"
    elif average < 100:
        return "WARNING"
    else:
        return "CRITICAL"

def main():
    execution_log.clear()

    print("\nGenerated Equipment Data:")
    readings = generate_readings()
    print(readings)

    print("\nValidation Results:")
    valid, invalid = validate_readings(readings)
    print("Valid:", valid)
    print("Invalid:", invalid)

    print("\nDiagnostic Results:")
    average = calculate_average(valid)
    condition = classify_condition(average)
    print("Average reading:", average)
    print("Condition:", condition)

    print("\nExecution Log:")
    for entry in execution_log:
        print(entry)

    print("\nFinal Output:")
    print(f"{len(valid)} valid / {len(invalid)} invalid readings processed.")
    print(f"Equipment status: {condition}")

if __name__ == "__main__":
    main()
