# reducer.py
import sys

movie_ratings = {}

for line in sys.stdin:
    movie_id, rating, count = line.strip().split("\t")
    if movie_id not in movie_ratings:
        movie_ratings[movie_id] = [0, 0]  # total_rating, count
    movie_ratings[movie_id][0] += float(rating)
    movie_ratings[movie_id][1] += int(count)

for movie_id, (total_rating, count) in movie_ratings.items():
    average_rating = total_rating / count
    print(f"{movie_id}\t{average_rating}")
