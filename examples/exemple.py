import sys
from pathlib import Path
import inspect

if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10]

    #%% unproper relative way
    # This script demonstrates a relative import, where a package that is not in the root or a subfolder of the Python
    # program is forcibly loaded.
    # Typically, individuals place a file containing functions in the root or a subfolder of the Python script being
    # used and import it without utilizing this workaround.
    relative_path = str(Path(__file__).resolve().parent.parent / 'src')
    sys.path.append(relative_path)
    from src.mypackage.module0 import calculate_rms
    sys.path.remove(relative_path)

    # print where is located the calculate_rms function
    rms_value = calculate_rms(numbers)
    print(f"Package relative local import : RMS of {numbers} is {rms_value}")
    print(f"calculate_rms is located in: {inspect.getfile(calculate_rms)}")

    #%% direct import and easy way :
    from mypackage.module0 import calculate_rms

    # print where is located the calculate_rms function
    rms_value = calculate_rms(numbers)
    print(f"/nPackage direct import : RMS of {numbers} is {rms_value}")
    print(f"calculate_rms is located in: {inspect.getfile(calculate_rms)}")
    print(f'The function is actually installed into your python environnement now')
