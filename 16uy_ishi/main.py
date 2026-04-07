import json
def load(fl="/Users/probox/ayyub/uy_ishlar/16uy_ishi/menu.json") -> list:
    with open(fl, "r") as file:
        return json.load(file)

def save(menus:list, fl="menu.json") -> None:
    with open(fl, "w") as file:
        return json.dump(menus, file, indent=4)
    
def add_product():
    name = input("nomi: ")
    price = int(input("narxi: "))
    menu = load()
    menu.append({"name": name, "price": price, "old_price": 0, "discount": 0})
    save(menu)
    show_admin_menu()

def check_admin_exists(admin_id:int):
    admins = load("admins.json")
    for person in admins:
        if person["admin_id"] == admin_id:
            print(f"admin topildi: {person['admin_name']}")
            show_admin_menu()
    print("admin topilmadi")
    show_admin_menu()
       
def set_food_discount(food_name:str, discount_percent:int) -> None:
    menu = load()
    for product in menu:
        if product["name"] == food_name:
            product["old_price"] = product["price"]
            product["discount"] = discount_percent
            product["price"] *= (1 - 0.01*discount_percent)
            save(menu)
            print(f"{product['name']} uchub {discount_percent}% chegirma qo'llandi. Ynagi narxi {product['price']}")
    show_admin_menu()

def get_most_ordered_food()-> None: 
    orders = load("/Users/probox/ayyub/uy_ishlar/16uy_ishi/orders.json")
    order = max(orders, key=lambda x: x["quantity"])
    print(f"Eng ko‘p buyurtma qilingan taom: {order['food_name']} ({order['quantity']} dona)")
    show_admin_menu()

def get_orders_by_user(user_id:int):
    users = load("orders.json")
    for user in users:
        if user["user_id"] == user_id:
            print(f"{user['food_name']} — {user['quantity']} dona — {user['price'] * user['quantity']} so‘m — {user["datetime"]}")
    show_admin_menu()

def filter_orders_by_date(date_part:str):
    dct = {}
    orders = load("/Users/probox/ayyub/uy_ishlar/16uy_ishi/orders.json")
    cnt = 0
    for order in orders:
        if date_part in order["datetime"]:
            dct[order["food_name"]] = order["quantity"]*order["price"]
            cnt+=1
    print(f"{cnt}ta buyurtma topildi:")
 
    n = 1
    for nomi, narxi in dct.items():
        print(f"{n}) {nomi} - {narxi} so'm")
        n+=1
    show_admin_menu()

def delete_order(order_id:int):
    orders = load("/Users/probox/ayyub/uy_ishlar/16uy_ishi/orders.json")
    index = 0
    for order in orders:
        if order_id == order["order_id"]:
            break
        index+=1
    else:
        print("bunday ID mavjud emas")   
        show_admin_menu()
    orders.pop(index)
    save(orders, "/Users/probox/ayyub/uy_ishlar/16uy_ishi/orders.json")
    show_admin_menu()

def delete_food(food_name):
    products = load("/Users/probox/ayyub/uy_ishlar/16uy_ishi/menu.json")
    index = 0
    for product in products:
        if food_name == product["name"]:
            break
        index+=1
    products.pop(index)
    save(products, "/Users/probox/ayyub/uy_ishlar/16uy_ishi/menu.json")
    show_admin_menu()

def get_max_discount_food():
    products = load()
    max_discount_product = max(products, key=lambda x: x["discount"])
    print(f"Eng katta chegirma: {max_discount_product["name"]} - {max_discount_product["discount"]}")
    show_admin_menu()

def show_menu():
    menu = load()
    for product in menu:
        print(f"{product["name"]:<20} {product["price"]:>10}")
    show_admin_menu()

def show_admin_menu():
    print(f"{'='*40}\n{'FAST FOOD ADMIN PANEL':^40}\n{'='*40}")
    print("1. Menyudagi barcha taomlarni ko‘rish\n2. Taomga chegirma qo‘yish\n3. Yangi taom qo‘shish\n4. Taomni o‘chirish\n5. Eng ko‘p buyurtma qilingan taom\n6. User buyurtmalarini ko‘rish\n7. Buyurtmani ID bo‘yicha o‘chirish\n8. Sana bo‘yicha buyurtmalarni filtrlash\n9. Eng katta chegirmaga ega taom\n10. Chiqish\n")
    n = int(input("Tanlang: "))
    while 1 > n or n > 10:
        n = int(input("\n1dan 10gacha.\nTanlang: "))

    if n == 1:
        show_menu()
    elif n == 2:
        name = input("taom nomi: ")
        discount = int(input("chegirma(%): "))
        set_food_discount(name, discount)
    elif n == 3:
        add_product()
    elif n == 4:
        name = input("qaysi taom: ")
        delete_food(name)
    elif n == 5:
        get_most_ordered_food()
    elif n == 6:
        id = int(input("user_id: "))
        get_orders_by_user(id)
    elif n == 7:
        id = int(input("order_id: "))
        delete_order(id)
    elif n == 8:
        date = input("(YYYY-MM-DD yoki YYYY-MM)\n>>> ")
        filter_orders_by_date(date)
    elif n == 9:
        get_max_discount_food()
    elif n == 10:
        return
    
    
show_admin_menu()
