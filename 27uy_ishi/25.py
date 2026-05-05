def max_movies_to_watch(movies: list) -> tuple:
    movies.sort(key=lambda x: x[1])
    
    result = []
    end = 0

    for start, finish in movies:
        if start >= end:
            result.append((start, finish))
            end = finish

    return len(result), result


movies = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
print(max_movies_to_watch(movies))
# Output: (3, [(1, 4), (5, 7), (8, 9)])

movies = [(1, 2), (2, 3), (3, 4), (4, 5)]
print(max_movies_to_watch(movies))
	# Output: (4, [(1, 2), (2, 3), (3, 4), (4, 5)])

movies = [(2, 6), (1, 5), (3, 7)]
print(max_movies_to_watch(movies))
	# Output: (1, [(1, 5)])

movies = []
print(max_movies_to_watch(movies))
	# Output: (0, [])

movies = [(2, 4), (0, 2), (4, 6), (6, 8)]
print(max_movies_to_watch(movies))
	# Output: (4, [(0, 2), (2, 4), (4, 6), (6, 8)])
