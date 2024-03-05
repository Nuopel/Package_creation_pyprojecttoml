import numpy as np

def calculate_rms(numbers):
    """
    Calculate the root mean square (RMS) of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The RMS value of the input numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")

    squared_values = [x ** 2 for x in numbers]
    mean_of_squares = np.mean(squared_values)
    return np.sqrt(mean_of_squares)


def print_hello():
    """
    This function prints the string "Hello, world!" to the console.
    It doesn't take any parameters or return any value.

    """
    print("Hello, world!")
