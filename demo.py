cart = []

def add_item():
    name = input("Item name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per item: "))
    cart.append({"name": name, "qty": qty, "price": price})

def bill():
    total = sum(item["qty"] * item["price"] for item in cart)
    discount = 0.1 * total if total > 1000 else 0
    print("\n---- Bill ----")
    for item in cart:
        print(f"{item['name']} x {item['qty']} = {item['qty'] * item['price']}")
    print(f"Total: {total}")
    print(f"Discount: {discount}")
    print(f"Payable: {total - discount}")

def menu():
    while True:
        print("\n1. Add Item\n2. Bill\n3. Exit")
        ch = int(input("Choice: "))
        if ch == 1:
            add_item()
        elif ch == 2:
            bill()
        elif ch == 3:
            break
        else:
            print("Invalid choice. Please try again.")

menu()