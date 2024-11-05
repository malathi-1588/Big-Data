# reducer.py
import sys

from collections import defaultdict

item_count = defaultdict(int)

for line in sys.stdin:
    candidate, count = line.strip().split("\t")
    item_count[candidate] += int(count)

# Print candidates that meet the support threshold
support_threshold = 3  # Example threshold
for itemset, count in item_count.items():
    if count >= support_threshold:
        print(f"{itemset}\t{count}")
