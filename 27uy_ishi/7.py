def get_phone_number(contacts: dict[str, str], search_name: str) -> str:
    return contacts[search_name] if search_name in contacts else "Topilmadi"


contacts = {}
search_name = "Ali"
print(get_phone_number(contacts, search_name))

# Output: Topilmadi

contacts = {
    "Ali": "+998901112233",
    "Vali": "+998909998877",
    "Hasan": "+998938889900"
}

search_name = "Vali"
print(get_phone_number(contacts, search_name))
# Output: +998909998877

search_name = "Ali"
print(get_phone_number(contacts, search_name))
# Output: +998901112233

