""" Program of game rock paper and scissors. This program ask user by to choose
a move by giving four options. Then computer chooses random move and result
is added. First to 5 point wins the game. User can choose to play the game
Again. """

# Importing the random module for computer choice
import random


def compare_two_moves(user_move, computer_move):
    """ Function to compare moves and return variable
        0 means that match is tie
        1 means that user won the match
        -1 means that computer won the match"""

    # If both the options are equal, then game is tie
    if user_move == computer_move:
        print(f"Both players selected {user_move}. It's a tie!")
        return 0

    # If statements when the user chooses rock
    # Along with determining the winner, these statements also increment the
    # user and computer wins variable accordingly
    if user_move == "rock":
        # If the computer chooses scissors, then the user wins
        if computer_move == "scissors":
            print("Rock smashes scissors! You win!")
            return 1

        # If the computer chooses paper, then the user loses
        print("Paper covers rock! You lose.")

    # If statements when the user chooses paper
    # Along with determining the winner, these statements also increment the
    # user and computer wins variable accordingly
    if user_move == "paper":
        # If the computer chooses rock, then the user wins
        if computer_move == "rock":
            print("Paper covers rock! You win!")
            return 1

        # If the computer chooses scissors, then the user loses
        print("Scissors cuts paper! You lose.")

    # If statements when the user chooses scissors
    # Along with determining the winner, these statements also increment the
    # user and computer wins variable accordingly
    if user_move == "scissors":
        # If the computer chooses paper, then the user wins
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
            return 1

        # If the computer chooses rock, then the user loses
        print("Rock smashes scissors! You lose.")

    return -1


# Three variables for total games, wins of user and wins of computer
TOTAL_GAMES = 0
USER_WINS = 0
COMPUTER_WINS = 0

if __name__ == "__main__":
    # Game loop which is an infinite loop
    while True:
        # try block to get the user input and check for any errors
        try:
            # Printing the UI for the user to make the move
            print("""\nMake Your Move:
                1. Rock
                2. Paper
                3. Scissors
                4. Quit""")

            # Taking the user of input and converting it to an integer
            user_input_choice = int(input("Enter a choice : "))

            # If the user chooses to quit, then the total games played along
            # with the number of wins for both user and computer are printed
            if user_input_choice == 4:

                # printing all the variables of the program
                print("\n\nTotal Games Played:", TOTAL_GAMES)
                print("Games won by user:", USER_WINS)
                print("Games won by computer:", COMPUTER_WINS)
                print("\nThanks for Playing !!")
                print("Terminating Game....")
                break

            # List of possible options in the game
            user_options_list = ["rock", "paper", "scissors"]

            # Generating the random choice of computer
            computer_choice = random.choice(user_options_list)

            # Assigning the user choice using the given list
            user_choice = user_options_list[user_input_choice-1]

        # Except block if user enters any value that is not a number
        except ValueError:
            print("Not a valid integer")
            print("Please enter a integer value between 1 and 4")
            # continue to skip the loop iteration
            continue

        # Except block if user enters integer that is not an option
        except IndexError:
            print("Invalid Option selected choice")
            print("Please type a number between 1 and 4")
            continue

        # Printing the options chosen by the user and computer
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")

        # Comparing move from user and computer
        RESULT_OF_COMPARISON = compare_two_moves(user_choice, computer_choice)

        # Increamenting the user wins variable if user won
        if RESULT_OF_COMPARISON == 1:
            USER_WINS += 1

        # Increamenting the computer wins variable if computer won
        elif RESULT_OF_COMPARISON == -1:
            COMPUTER_WINS += 1

        # Incrementing the total games variable
        TOTAL_GAMES += 1

        # If any of the wins are equal to 5, then the match ends
        # and total games are printed
        if USER_WINS == 5 or COMPUTER_WINS == 5:

            # Printing message when match is won by user
            if USER_WINS == 5:
                print("\n\nCongrats!! You are the winner!")
                print("Total Games Played:", TOTAL_GAMES)

            # Printing message when match is won by Computer
            else:
                print("\n\nComputer is the winner!\nBetter Luck Next Time!!")
                print("Total Games Played:", TOTAL_GAMES)

            # Resetting the variables for the next match
            TOTAL_GAMES = 0
            USER_WINS = 0
            COMPUTER_WINS = 0

            # Asking user if for playing again
            play_again = input("\nWant to play one more game? (y/n): ")
            # If the user enters anything other than 'y' or 'Y'
            # the game is terminated
            if play_again.lower() != "y":
                print("\nThanks for Playing !!")
                print("Terminating Game....")
                break
