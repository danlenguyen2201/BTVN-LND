# items.remove("Phở gánh")
# print(items)
#
# items.pop(3)
# print(items)
items = ["T-shirt","Jeans","Sweater","Pants","Gun","Sword"]

print("Welcome t’o our shop, what do you want ?")
print("Down here are the choices :D")
print("1: Add new item to the shop")
print("2: See our items")
print("3: Update an item name")
print("4: Delete an item in the shop")
print("5: Exit")
print("Please enter a number!")
loop_continue = True
while loop_continue:
    choice = int(input(">> "))
    def print_items():
        item_no = 1
        for item in items:
            print("#", end="")
            print(item_no, end =". ")
            print(item)
            item_no += 1
    if choice == 1:
        new_item = input("Enter the new item name:")
        items.append(new_item)
        print("The items list have been update to this")
        print(items)
        print("Anything else?")
        print_items()
    elif choice == 2:
        print("Here are our items")
        print_items()
        print("Anything else?")
        print_items()
    elif choice == 3:
        print_items()
        position = int(input("What position ?"))
        new_item_name = input("Please enter the new name:")
        items[position - 1] = new_item_name
        print(items)
        print("The name of the item have been updated")
        print("Anything else?")
        print_items()
    elif choice == 4:
        print_items()
        position = int(input("Qhat position do you want to delete ?"))
        items.pop(position - 1)
        print("The list have been updated")
        print(items)
        print("Anything else?")
        print_items()
    elif choice == 5:
        print("Thank you for doing business with us,good bye and have a good day! ")
        loop_continue = False

    else:
        print("Sorry but you have choosed the wrong choice, please choose again!")
        print("1: Add new item to the shop")
        print("2: See our items")
        print("3: Update an item name")
        print("4: Delete an item in the shop")
        print("5: Exit")