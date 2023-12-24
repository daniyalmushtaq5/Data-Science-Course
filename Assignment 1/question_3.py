print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')

if choice_1.lower() == "left":
    choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" toswim across. \n')

    if choice_2.lower() == "wait":
        choice_3 = input("In which door do you want to go? Type 'red', 'blue' or 'yellow' \n")

        if choice_3.lower() == "red":
            print("Burned by fire. \n Game Over")

        elif choice_3.lower() == "blue":
            print("Eaten by beasts. \n Game Over")

        elif choice_3.lower() == "yellow":
            print("You Win")

        else:
            print("Game Over")

    else:
        print("Attacked by trout. \n Game Over")
else:
    print("Fall into a hole \n Game Over")