def find_nearest_vowel(letter: str) -> str:
    if not letter.islower() or len(letter) > 1 :
        return "faqat bitta kichik harf bo‘lishi kerak"
    dct = {
        "a" : 97,
        "e" : 101,
        "u" : 117,
        "i" : 105,
        "o" : 111
    }

    return min(dct, key=lambda x: abs(dct[x] - ord(letter)))

print(find_nearest_vowel("k"))  
# Output: i


letter = "e"
print(find_nearest_vowel(letter))  
# Output: e

letter = "c"
print(find_nearest_vowel(letter)) 
# Output: a

letter = "z"
print(find_nearest_vowel(letter)) 
# Output: u

letter = "h"
print(find_nearest_vowel(letter)) 
# Output: i

letter = "K"
print(find_nearest_vowel(letter))  
# Output: faqat bitta kichik harf bo‘lishi kerak 

letter = "4"
print(find_nearest_vowel(letter)) 
# Output: faqat bitta kichik harf bo‘lishi kerak 

letter = "%"
print(find_nearest_vowel(letter))  
# Output: faqat bitta kichik harf bo‘lishi kerak 

letter = "ha"
print(find_nearest_vowel(letter)) 
# Output: faqat bitta kichik harf bo‘lishi kerak