def ends_with_gram(words: list[str]) -> list[str]:
    result = []
    for word in words:
        if word.endswith("gram"):
            result.append(word)
    return result

words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
print(ends_with_gram(words))
# Output: ['telegram', 'Instagram', 'program', 'diagram']
print(ends_with_gram(["telegram", "world", "program"]))
print(ends_with_gram(["photo", "diagram", "Instagram"]))
print(ends_with_gram(["code", "test", "function"]))
print(ends_with_gram(["Gram", "telegram"]))
print(ends_with_gram([]))
