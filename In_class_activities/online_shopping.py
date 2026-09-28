class Product:
    def __init__(self, name, price, catagory, stock):
        self.name = name
        self.price = price
        self.catagory = catagory
        self.stock = stock

    def show_detail(self):
        print(f"{self.name} - ${self.price} - {self.catagory} - Stock: {self.stock}")

products=[
    Product("Laptop", 1000, "Electronics", 10),
    Product("Headphones", 100, "Electronics", 20),
    Product("Keyboard", 800, "Accessories", 15),
    Product("Mouse", 50, "Accessories", 30),
    Product("Schoole Bag", 100, "Stationary", 30)
]

def show_products():
    print("Product Catalogue:")

    for index, product in enumerate(products, start=1):
        print(
            f"{index}. {product.name} |"
            f"{product.price} |"
            f"{product.catagory} |"
            f"Stock: {product.stock}"

        )
cart=[]

def add_to_cart():
    show_products()
    choice = int(input("Enter the product number"))

    if choice < 1 or choice > len(products):
        print("!!Invalid product number!!")
        return
    
    product = products[choice - 1]

    quantity = int (input(f"Enter the quantity:"))

    if quantity <=0:
        print("The quantity must be greater than zero!!")

    elif quantity > product.stock:
        print("!!Insufficient stock!!")
        return
    else:
        cart.append((product, quantity))
        product.stock -= quantity

        print(f"{quantity} - {product.name} added ro cart successfully!!")


def show_cart():
    if len(cart)==0:
        print("Your cart is empty!!")
        return
    print("Your Cart:")
    total=0

    for product, quantity in cart:
        item_total = product.price * quantity
        total += item_total

        print(
            f"{product.name} - {quantity}"
            f"= ${item_total}"
        )

    print(f"Total: ${total}")


def calculate_discount(total):
    if total >= 1000:
        discount= total * 0.05

    elif total >= 2000:
        discount = total * 0.10

    else:
        discount = 0
    return discount

def checkout():
    if len(cart)==0:
        print("Your cart is empty!!")
        return
    subtotal=0

    for product, quantity in cart:
        subtotal += product.price * quantity

    discount= calculate_discount(subtotal)

    final_amount= subtotal - discount
    payment_methods = ("UPI", "Credit Card", "Debit Card", "Cash on Delivery")

    print("\n========== CHECKOUT ==========")

    print(f"Subtotal : ₹{subtotal}") ,print(f"Discount : ₹{discount}")

    print(f"Final Amount : ₹{final_amount}")

    print("\nPayment Methods:")

    for method in payment_methods:

        print("-", method)

    payment = input("\nChoose payment method: ")

    if payment in payment_methods:
        print("\nPayment successful!")
        print(f"Amount paid: ₹{final_amount}")
        print("Thank you for shopping with us!")
        cart.clear()

    else:
        print("Invalid payment method.")

def show_categories():

    categories = set()

    for product in products:

        categories.add(product.catagory)

    print("\n========== CATEGORIES ==========")

    for category in categories:

        print("-", category)
while True:

    print("\n================================")

    print(" ONLINE SHOPPING")

    print("================================")

    print("1. View Products")

    print("2. View Categories")

    print("3. Add Product to Cart")

    print("4. View Cart")

    print("5. Checkout")

    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        show_categories()
    elif choice == "3":
        add_to_cart()
    elif choice == "4":
        show_cart() 
    elif choice == "5":
        checkout()      
    elif choice == "6":
        print("Thank you for visiting our online store!")
        break
    else:
        print("Invalid choice. Please try again.")


