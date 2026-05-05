def caesar_cipher_numbers(numbers: list) -> list:
    dct = {
        "1" : "4",
        "2" : "5",
        "3" : "6",
        "4" : "7",
        "5" : "8",
        "6" : "9",
        "7" : "0",
        "8" : "1",
        "9" : "2",
        "0" : "3",
        
        
    }
    for i in range(len(numbers)):
        shifr =""
        for j in range(len(numbers[i])):
            shifr += dct[numbers[i][j]]
        numbers[i] = shifr

    return numbers



numbers = [
    "37412",
    "9999",
    "12345",
    "0000",
    "56789"
]

print(caesar_cipher_numbers(numbers))