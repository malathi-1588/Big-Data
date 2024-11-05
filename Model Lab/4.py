# Problem: Calculate Average Ratings
# Problem Statement: Compute the average rating for each movie from a dataset of ratings.
# mapper.py
import sys

for line in sys.stdin:
    user_id, movie_id, rating = line.strip().split(",")
    print(f"{movie_id}\t{rating}\t1")  # Emit movie_id, rating, and count of 1

