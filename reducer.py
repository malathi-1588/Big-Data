#!/usr/bin/env python3
import sys

min_temp = float('inf')
max_temp = float('-inf')

for line in sys.stdin:
    key, value = line.strip().split('\t')
    value = float(value)
    
    if key == "min":
        if value < min_temp:
            min_temp = value
    elif key == "max":
        if value > max_temp:
            max_temp = value
            
print(f"Minimum Temperature: {min_temp}")
print(f"Maximum Temperature: {max_temp}")

