from mypackage.module0 import calculate_rms


if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]
    rms_value = calculate_rms(numbers)
    print(f"RMS of {numbers} is {rms_value}")