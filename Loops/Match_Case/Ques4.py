
operation=input("Enter the Menu food item (Burger, Pizza, Fries, Soda): ")

number=int(input("Enter a number:"))


match(operation):
    case"Burger":
        print(f"You have ordered a Burger for {number*50} Rs")
    case"Pizza":
        print(f"You have ordered a Pizza for {number*100} Rs")
    case"Fries":
        print(f"You have ordered Fries for {number*30} Rs")
    case"Soda":
        print(f"You have ordered a Soda for {number*20} Rs")
    case _:
        print("Item not available")

