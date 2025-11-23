import csv
import os

# ----------- Auto receipt numbering ----------
def get_receipt_number():
    if not os.path.exists("receipt_count.txt"):
        with open("receipt_count.txt", "w") as f:
            f.write("0")

    with open("receipt_count.txt", "r") as f:
        count = int(f.read().strip())

    count += 1

    with open("receipt_count.txt", "w") as f:
        f.write(str(count))

    return f"Bill{count:03d}"


# ----------- Initial items (fruits already stored) ----------
items = [
    {"name": "Apple", "price": 50, "quantity": 10, "discount": 10},
    {"name": "Banana", "price": 10, "quantity": 20, "discount": 0},
    {"name": "Mango", "price": 80, "quantity": 15, "discount": 5},
    {"name": "Orange", "price": 40, "quantity": 12, "discount": 8},
    {"name": "Grapes", "price": 60, "quantity": 18, "discount": 12},
    {"name": "Pineapple", "price": 90, "quantity": 5, "discount": 15}
]


# ------------------ GROCERY SYSTEM -------------------------
while True:
    input("Press ENTER to continue...")
    print('------------------Welcome to the Grocery Store------------------')
    print('1. View items')
    print('2. Add items for sale')
    print('3. Purchase items (Shopping Cart)')
    print('4. Search items')
    print('5. Edit items')
    print('6. Exit')

    choice = input("Enter your choice: ")

    # ------------------ VIEW ITEMS ------------------
    if choice == '1':
        print("\n------------------AVAILABLE ITEMS------------------")
        for item in items:
            print(f"{item['name']}  | Price: {item['price']} | Qty: {item['quantity']} | Discount: {item['discount']}%")
        print()

    # ------------------ ADD ITEMS ------------------
    elif choice == '2':
        print("\n------------------ADD NEW ITEM------------------")

        new_item = {}
        new_item['name'] = input("Item name: ")

        while True:
            try:
                new_item['price'] = float(input("Price: "))
                break
            except:
                print("Invalid price. Enter again.")

        while True:
            try:
                new_item['quantity'] = int(input("Quantity: "))
                break
            except:
                print("Invalid quantity. Enter again.")

        while True:
            try:
                new_item['discount'] = float(input("Discount %: "))
                break
            except:
                print("Invalid discount. Enter again.")

        items.append(new_item)
        print("Item added successfully.\n")

    # ------------------ SHOPPING CART ------------------
    elif choice == '3':
        print("\n------------------SHOPPING CART------------------")

        cart = []

        while True:
            print("\nAvailable Items:")
            for item in items:
                print(f"- {item['name']} (${item['price']}) Qty: {item['quantity']} Discount: {item['discount']}%")

            selected = input("\nEnter item to add to cart OR type 'done': ")

            if selected.lower() == "done":
                break

            found = False
            for item in items:
                if selected.lower() == item["name"].lower():
                    found = True
                    if item["quantity"] > 0:
                        cart.append(item)
                        item["quantity"] -= 1
                        print(f"Added {item['name']} to cart.")
                    else:
                        print("Item out of stock.")
                    break

            if not found:
                print("Item not found.")

        if len(cart) == 0:
            print("Cart is empty. No purchase made.\n")
            continue

        # ----------- Generate receipt ----------
        receipt_no = get_receipt_number()
        filename = f"{receipt_no}.csv"
        total_amount = 0

        print("\nGenerating receipt...")

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Item", "Price", "Discount %", "Discount Amount", "Final Price"])

            for item in cart:
                discount_amt = item['price'] * (item['discount'] / 100)
                final_price = item['price'] - discount_amt
                total_amount += final_price

                writer.writerow([item['name'], item['price'], item['discount'], discount_amt, final_price])

            writer.writerow([])
            writer.writerow(["TOTAL AMOUNT", total_amount])

        print("\n------------------BILL SUMMARY------------------")
        print(f"Receipt Number: {receipt_no}")
        print(f"Total Amount Payable: ₹{total_amount}")
        print(f"Receipt saved as: {filename}\n")

    # ------------------ SEARCH ITEM ------------------
    elif choice == '4':
        find = input("Enter item name to search: ")

        for item in items:
            if item["name"].lower() == find.lower():
                print("Item found:", item)
                break
        else:
            print("Item not found.\n")

    # ------------------ EDIT ITEM ------------------
    elif choice == '5':
        edit = input("Enter item name to edit: ")

        for item in items:
            if item['name'].lower() == edit.lower():
                print("Current details:", item)
                
                item['name'] = input("New name: ")
                item['price'] = float(input("New price: "))
                item['quantity'] = int(input("New quantity: "))
                item['discount'] = float(input("New discount %: "))

                print("Item updated successfully.\n")
                break
        else:
            print("Item not found.\n")

    # ------------------ EXIT ------------------
    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid option.\n")
