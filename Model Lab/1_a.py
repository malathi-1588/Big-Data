import sys
from collections import defaultdict

word_count = defaultdict(int)

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()  # Strip whitespace
    if not line:  # Skip empty lines
        continue
    try:
        word, count = line.split("\t")  # Split the line into word and count
        word_count[word] += int(count)  # Increment the count for the word
    except ValueError:  # Handle invalid lines
        print(f"Skipping invalid line: {line}", file=sys.stderr)

# Output the total counts for each word
for word, count in word_count.items():
    print(f"{word}\t{count}")
