def format_date(date_str: str) -> str:
    dct = {
    "01": "yanvar",
    "02": "fevral",
    "03": "mart",
    "04": "aprel",
    "05": "may",
    "06": "iyun",
    "07": "iyul",
    "08": "avgust",
    "09": "sentyabr",
    "10": "oktabr",
    "11": "noyabr",
    "12": "dekabr"
    }
    kun, oy, yil = date_str.split(".")
    return f"{int(kun)} {dct[oy]} {yil} yil"

# Test
print(format_date("13.02.2025"))
# Output: 13 Fevral 2025 yil

print(format_date("01.01.2000"))
# Output: 1 Yanvar 2000 yil

print(format_date("15.03.1995"))
# Output: 15 Mart 1995 yil

print(format_date("30.12.2024"))
# Output: 30 Dekabr 2024 yil

print(format_date("09.07.2010"))
# Output: 9 Iyul 2010 yil
