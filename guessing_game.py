"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random 

# Keep messages to user consistent and less DRY
def user_notification(message):
    print("-" * 15)
    print(message)
    print("-" * 15)


def start_game():
    user_notification("Game Start: Please guess a number between 1 and 10.")
    # The game variables
    random_number = random.randint(1, 10)
    number_of_guesses = 0
    user_guess = 0
    while user_guess != random_number:
        try:
            # check what the user enters is an integer for comparison
            user_guess = int(input("What number would you like to guess? \n"))
            number_of_guesses += 1
            # prevent user from guessing outside the range
            if user_guess <= 0 or user_guess >= 11:
                raise Exception("That number is not between 1 and 10, please try again.")
        # prevent the user from entering numbers
        except ValueError:
            print("Please enter a number.")
        except Exception as e:
            print(e)        
        # if the try block succeeds respond higher or lower
        if user_guess > random_number:
            print("It's lower")
        elif user_guess < random_number:
            print("It's higher")
    if number_of_guesses >= 5:
        user_notification("You got it after {} gueses! :)\n Don't forget to pracice and thanks for playing!".format(number_of_guesses))
    else:
        user_notification("You got it after only {} gueses! :)\n Great Job and thanks for playing!".format(number_of_guesses))


start_game()