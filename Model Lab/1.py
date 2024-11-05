#!/usr/bin/env python

import sys

# Read from standard input
for line in sys.stdin:
    words = line.strip().split()  # Split the line into words
    for word in words:
        print(f"{word}\t1")  # Output each word with a count of 1
