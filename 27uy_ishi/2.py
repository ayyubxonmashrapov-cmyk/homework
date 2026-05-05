def search_by_genre(cinema: list, genre: str) -> list:
    result = []
    for film in cinema:
        if film["genre"] == genre:
            result.append(film)

    return result

cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]

print(search_by_genre(cinema, "Fantastika"))
# Output:
# [
#   {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#   {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]

print(search_by_genre(cinema, "Drama"))
# Output:
# [{"title": "Oq yo‘l", "genre": "Drama", "price": 25000}]

print(search_by_genre(cinema, "Komediya"))
# Output:
# []


print(search_by_genre([], "Boevik"))
# Output: []

print(search_by_genre(cinema, "Detektiv"))
# Output: [{"title": "Sherlock", "genre": "Detektiv", "price": 30000}]
