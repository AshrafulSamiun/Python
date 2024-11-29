# Project : Favorit Food Manager

favourite_foods = []  # initialize empty list for favourite foods

while True:
    print("Favourite Food Manager")
    print("0. Exit")
    print("1. Add Food")
    print("2. Remove Food")
    print("3. Display Foods")

    chioce=input("Choice an Option")

    if chioce=="0":
        print("Thanks for Choosing Favorit Food Manager")
        break
    elif chioce=="1":
        food=input("Enter Your Favorit Food Name")
        favourite_foods.append(food)
        print(f"{food} Food Added Successfully")
    elif chioce=="2":
        food = input("Enter Your Food Name which you want to remove")
        if food in favourite_foods:
            favourite_foods.remove(food)
            print(f"{food} Food Remove Successfully")
        else:
            print(f"{food} Food does exits in List")
    elif chioce=="3":
        if favourite_foods:
            print("Your Favorit Foods:")
            for index, food in enumerate(favourite_foods,start=1):
                print(f"{index} {food}")
        else:
            print("Food List is empty or didn't added yet!")
    else:
        print("Invalid Operation")


