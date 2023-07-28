"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random 

# Write your code inside this function.
def start_game():
    print("-" * 15)
    print("Game Start: Please guess a number between 1 and 10.")

    random_number = random.randint(1, 10)
    number_of_guesses = 0
    user_guess = 0

    while user_guess != random_number:
        try:
            user_guess = int(input("What number would you like to guess? \n"))
            if user_guess <= 0 or user_guess >= 11:
                raise Exception("That number is not between 1 and 10, please try again.")
        except ValueError:
            print("Please enter a number.")
        except Exception as e:
            print(e)        

        if user_guess > random_number:
            print("It's lower")
        elif user_guess < random_number:
            print("It's higher")
        number_of_guesses += 1
        
    print("You got it!")
    print("Game End: Thank you for playing!")
    print("-" * 15)



#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()