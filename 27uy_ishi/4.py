def format_date(date_str: str) -> str:
    dct = {
        "yanvar" : "01",
        "fevral" : "02",
        "mart" : "03",
        "aprel" : "04",
        "may" : "05",
        "iyun" : "06",
        "iyul" : "07",
        "avgust" : "08",
        "sentyabr" : "09",
        "oktabr" : "10",
        "noyabr" : "11",
        "dekabr" : "12"
    }
    kun, oy, yil = date_str.split()

    if int(kun)/10 < 1:
        kun = "0"+kun

    return f"{kun}.{dct[oy]}.{yil[2:]}"



print(format_date("24 mart 2025"))
# Output: 24.03.25

print(format_date("24 mart 2025"))
# Output: 24.03.25

print(format_date("1 yanvar 2000"))
# Output: 01.01.00

print(format_date("15 iyul 1999"))
# Output: 15.07.99

print(format_date("9 sentyabr 2010"))
# Output: 09.09.10

print(format_date("30 dekabr 2024"))
# Output: 30.12.24
