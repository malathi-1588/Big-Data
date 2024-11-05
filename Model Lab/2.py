# mapper.py
import sys

for line in sys.stdin:
    data = line.strip().split(",")  # Assuming CSV format
    if len(data) > 1:
        try:
            temperature = float(data[1])  # Assuming temperature is in the second column
            print(f"max\t{temperature}")
            print(f"min\t{temperature}")
        except ValueError:
            continue

