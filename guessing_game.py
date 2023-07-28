"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random 


def start_game(current_high_score):
    print("-" * 15)
    print("Game Start: Please guess a number between 1 and 10.")
    print("The current high score is {}.".format(current_high_score))
    # The game variables
    random_number = random.randint(1, 10)
    number_of_guesses = 0
    user_guess = 0
    while user_guess != random_number:
        try:
            # Check what the user enters is an integer for comparison
            user_guess = int(input("What number would you like to guess? \n"))
            number_of_guesses += 1
            # Prevent user from guessing outside the range
            if user_guess <= 0 or user_guess >= 11:
                raise Exception("That number is not between 1 and 10, please try again.")
        # Prevent the user from entering numbers
        except ValueError:
            print("Please enter a number.")
        except Exception as e:
            print(e)        
        # If the try block succeeds respond higher or lower
        if user_guess > random_number:
            print("It's lower")
        elif user_guess < random_number:
            print("It's higher")

    # Congratulate the user if they beat the high score
    if number_of_guesses < current_high_score:
        print("Congrats!! you scored {} beating the original high score {}.".format(number_of_guesses, current_high_score)) 
    elif number_of_guesses == current_high_score:
        print("Congrats!! you scored {} beating the matching the high score {}.".format(number_of_guesses, current_high_score))
    else:
        print("You scored {} therefore not beating the high score of {}.".format(number_of_guesses, current_high_score))         
    # See if the user wants to play again
    play_again = input("Would you like to play again? Y/N\n")
    if play_again.upper() == "Y":
        # Start game again
        start_game(number_of_guesses)
    else:
        print("-" * 15)
        print("Have a great day! Ending program.")


# Start game and decide the original high score
start_game(4)