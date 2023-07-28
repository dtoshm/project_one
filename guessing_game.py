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


def start_game(current_high_score):
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

    # Congratulate the user if they beat the high score
    if number_of_guesses < current_high_score:
        user_notification("Congrats!! you scored {} beating the original high score {}.".format(number_of_guesses, current_high_score)) 
    elif number_of_guesses == current_high_score:
        user_notification("Congrats!! you scored {} beating the matching the high score {}.".format(number_of_guesses, current_high_score))
    else:
        user_notification("You scored {} therefore not beating the high score of {}.".format(number_of_guesses, current_high_score))         
    # See if the user wants to play again
    play_again = input("Would you like to play again? Y/N\n")
    if play_again.upper() == "Y":
        # Start game again
        start_game(number_of_guesses)
    else:
        user_notification("Have a great day! Ending program.")

# Start game and decide what the high score will be
start_game(4)