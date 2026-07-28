menu = {
    'pizza' : 1250,
    'burger' : 140,
    'pasta': 250,
    'salad': 80,
    'coffee': 60,
    'layz\n': 70,
}
print("Welcome to My Yummy restaurant! Here is our menu\n")
print("Pizza: RS 1250\nBurger: RS140\npasta: RS250\nsalad: RS80\ncoffee: RS60\nLayz: RS50")

order_total = 0

item_1 = input("Enetr the name of  item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"Sorry, Ordered item {item_1} is not available Yet!")

another_order = input("Do you want to order another item? (yes/no): ")
if another_order == 'yes':
    item_2 = input("Enter the name of your second item order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"Sorry, Your Ordered item {item_2} is not available in our menu.")
    print(f"The total amount of items to pay is {order_total} ")
