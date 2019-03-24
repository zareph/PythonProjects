def main():

    import random

    def start_over():
        if roll_again == "no" or roll_again == "n":
            main()
        else:
            exit()

    print("Dice selection:")
    print("1: Roll a six-sided dice")
    print("2: Roll a D20")
    print("3: Random Number Generator")
    selection = input(">> ")

    if selection == "1":
        min = 1
        max = 6
        roll_again = "yes"
        while roll_again == "yes" or roll_again == "y":
            print("\nLet's toss some dice!")
            print("You rolled a " + str(random.randint(min, max)) + ".")

            roll_again = input("Roll again? (y/n) >> ").lower()
        start_over()

    elif selection == "2":
        min = 1
        max = 20
        roll_again = "yes"
        while roll_again == "yes" or roll_again == "y":
            print("\nLet's toss some dice!")
            print("You rolled a " + str(random.randint(min, max)) + ".")

            roll_again = input("Roll again? (y/n) >> ").lower()
        start_over()

    elif selection == "3":
        min = int(input("Select minimum number: "))
        max = int(input("Select maximum number: "))
        roll_again = "yes"
        while roll_again == "yes" or roll_again == "y":
            print("\nGenerating random number...")
            print("Your number is: " + str(random.randint(min, max)) + ".")

            roll_again = input("Try again? (y/n) >> ").lower()
        start_over()
    else:
        return
            
main()