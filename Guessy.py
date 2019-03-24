import random
import sys

print("\nWelcome to the Guess The Number game.\n")

def main():

    print("I am thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)

    attempts = 5
    remaining_attempts = 5

    for attempt in range(attempts):
        
        guess = input(">> ")

        if guess == "exit" or guess == "quit":
            sys.exit()

        elif guess.isdigit() == False or int(guess) > 100 or int(guess) < 1:
            print("\nInvalid number.\n")
            main()

        elif int(guess) == random_number:
            print("\nYou guessed the right number! Congratulations.\n")
            main()

        elif int(guess) < random_number:
            remaining_attempts -= 1
            if remaining_attempts == 0:
                break
            else:
                print("Too low! You have " + str(remaining_attempts) + " attempt(s) remaining.")
            
        elif int(guess) > random_number:
            remaining_attempts -= 1
            if remaining_attempts == 0:
                break
            else:
                print("Too high! You have " + str(remaining_attempts) + " attempt(s) remaining.")

    if int(guess) != random_number:
        print("\nSorry, you've reached the maximum number of attempts.")
        print("The secret number was: " + str(random_number) + ".\n")

        main()
    
main()