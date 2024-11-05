from itertools import combinations
import sys

# mapper.py
def generate_candidates(transactions, k):
    candidates = set()
    for transaction in transactions:
        for combo in combinations(sorted(transaction), k):
            candidates.add(combo)
    return candidates

for line in sys.stdin:
    transaction = line.strip().split(",")  # Assuming transactions are comma-separated
    # Emit all pairs of items as potential candidates
    candidates = generate_candidates([transaction], 2)
    for candidate in candidates:
        print(f"{candidate}\t1")

