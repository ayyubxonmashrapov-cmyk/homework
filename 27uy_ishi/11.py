def check_anagram(word1: str, word2: str) -> bool:
    return set(word1.lower()) == set(word2.lower())

word1 = "listen"
word2 = "silent"
print(check_anagram(word1, word2))

word1 = "hello"
word2 = "world"
print(check_anagram(word1, word2))
word1 = "triangle"
word2 = "integral"
print(check_anagram(word1, word2))
word1 = "rat"
word2 = "tar"
print(check_anagram(word1, word2))
word1 = "abc"
word2 = "def"
print(check_anagram(word1, word2))
word1 = "Aba"
word2 = "aBa"
print(check_anagram(word1, word2))
word1 = ""
word2 = ""
print(check_anagram(word1, word2))
word1 = "a"
word2 = "A"
print(check_anagram(word1, word2))
word1 = "ab"
word2 = "a"
print(check_anagram(word1, word2))
word1 = "debit card"
word2 = "bad credit"
print(check_anagram(word1, word2))

