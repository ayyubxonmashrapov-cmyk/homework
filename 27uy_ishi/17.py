def decode_string(s: str) -> str:
    result = ""
    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha():
            result += s[i+1]*int(s[i])
    
    return result

print(decode_string("3a2b1c"))

print(decode_string("2x48y1z"))
print(decode_string("0a1b2c"))
print(decode_string(""))
print(decode_string("5d0e3f"))






