#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split(',')
    temperature = float(fields[2])
    # Emit the temperature for both min and max calculations
    print(f"min\t{temperature}")
    print(f"max\t{temperature}")


