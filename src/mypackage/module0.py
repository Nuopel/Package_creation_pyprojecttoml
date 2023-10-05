import numpy as np

def calculate_rms(numbers):
    """
    Calculate the root mean square (RMS) of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The RMS value of the input numbers.
    """
    if len(numbers) == 0:
        return 0.0

    squared_values = [x ** 2 for x in numbers]
    mean_of_squares = np.mean(squared_values)
    rms = np.sqrt(mean_of_squares)
    return rms