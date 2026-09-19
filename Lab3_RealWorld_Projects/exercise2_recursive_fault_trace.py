# Exercise 2: Recursive Fault Trace

# Student-specific inputs 
LASTNAME = "CAMPOS"
SEEDNUM = 7
FAVORITEARTIST = "CAR SEAT HEADREST"

call_count = 0   # counts how many times the recursive function runs
exercise_2_log = []

def generate_fault_code():
    exercise_2_log.append("[LOG] Generating fault code...")
    return sum(ord(c) for c in LASTNAME + FAVORITEARTIST) * SEEDNUM

def trace_fault(code):
    global call_count
    exercise_2_log.append(f"[LOG] Tracing fault code {code}...")
    print("Tracing:", code)

    if code < 10:             # base condition: stop at a single digit
        return code

    call_count += 1
    next_code = sum(int(d) for d in str(code))
    return trace_fault(next_code)

def main():
    global call_count
    call_count = 0
    exercise_2_log.clear()

    print("\nGenerated Fault Data:")
    fault_code = generate_fault_code()
    print("Fault code:", fault_code)

    print("\nRecursive Trace:")
    final_code = trace_fault(fault_code)

    print("\nNumber of Recursive Calls:")
    print(call_count)

    print("\nExecution Log:")
    for entry in exercise_2_log:
        print(entry)

    print("\nFinal Output:")
    print(f"Fault code {fault_code} reduced to {final_code} in {call_count} calls.")

if __name__ == "__main__":
    main()
