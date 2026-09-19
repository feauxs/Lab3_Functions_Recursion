# Exercise 3: Intelligent Equipment Monitoring Pipeline Entry point.
import telemetry_module
import diagnostics_module

def main():
    diagnostics_module.exercise_3_log.clear()

    print("LASTNAME:", telemetry_module.LASTNAME)
    print("SEEDNUM:", telemetry_module.SEEDNUM)
    print("FAVORITEARTIST:", telemetry_module.FAVORITEARTIST)

    print("\nGenerated Telemetry Data:")
    data_preview = list(telemetry_module.telemetry_stream())   # just to show/print the values
    print(data_preview)

    valid, invalid, abnormal = diagnostics_module.process_stream(telemetry_module.telemetry_stream())

    print("\nValid/Invalid Results:")
    print("Valid:", valid)
    print("Invalid:", invalid)

    print("\nProcessed Results:")
    print(f"Processed: {len(valid) + len(invalid)}")
    print(f"Valid: {len(valid)}  Invalid: {len(invalid)}  Abnormal: {len(abnormal)}")

    print("\nRecursive Analysis:")
    if abnormal:
        for original, steps, final_value in abnormal:
            print(f"{original} -> {steps} step(s) -> {final_value}")
    else:
        print("No abnormal readings.")

    status = "CRITICAL" if len(abnormal) > 2 else ("WARNING" if abnormal else "NORMAL")

    print("\nFinal Diagnostic Summary:")
    print(f"Overall Equipment Status: {status}")

    print("\nExecution Log:")
    for entry in diagnostics_module.exercise_3_log:
        print(entry)

    print("\nFinal Output:")
    print(f"Processed: {len(valid) + len(invalid)}")
    print(f"Valid: {len(valid)}  Invalid: {len(invalid)}  Abnormal: {len(abnormal)}")
    print(f"Overall Equipment Status: {status}")

if __name__ == "__main__":
    main()
