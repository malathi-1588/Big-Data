# reducer.py
import sys

max_temp = float('-inf')
min_temp = float('inf')

for line in sys.stdin:
    key, value = line.strip().split("\t")
    value = float(value)
    if key == "max":
        max_temp = max(max_temp, value)
    elif key == "min":
        min_temp = min(min_temp, value)

print(f"Max Temperature: {max_temp}")
print(f"Min Temperature: {min_temp}")
