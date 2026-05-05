def get_top_user(data: list[tuple[str, int]]) -> str:
    dct = {}
    for user in data:
        if user[0] in dct:
            dct[user[0]] += user[1]
        else:
            dct[user[0]] = user[1]

    return "" if not data else max(dct, key=lambda x: dct[x])

data = [
    ("user1", 50),
    ("user2", 60),
    ("user1", 40),
    ("user3", 30)
]
print(get_top_user(data))
# Output: user1

print(get_top_user([("u1", 100), ("u2", 150), ("u1", 50)]))
print(get_top_user([("ali", 30), ("vali", 20), ("ali", 70), ("vali", 90)]))
print(get_top_user([("a", 10)]))
print(get_top_user([]))
print(get_top_user([("x", 0), ("y", 0)]))


