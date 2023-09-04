# Needed to create random numbers to simulate dice roll
# import random

# # Initialise player scores to 0
# player1_score = 0
# player2_score = 0
# finish_line = 30

# # Repeat everything in this block 10 times
# for i in range(30):

#     # Generate random numbers between 1 and 6 for each player.
#     player1_value = random.randint(1, 6)
#     player2_value = random.randint(1, 6)

#     # Display the values
#     print("Player 1 rolled: ", player1_value)
#     print("Player 2 rolled: ", player2_value)

#     # Selection: based on comparison of the values, take the appropriate path through the code.
#     if player1_value > player2_value:
#         print("player 1 wins.")
#         player1_score = player1_score + 1  # This is how we increment a variable
#     elif player2_value > player1_value:
#         print("player 2 wins")
#         player2_score = player2_score + 1
#     else:
#         print("It's a draw")

#     input("Press enter to continue.")  # Wait for user input to proceed.

# print("### Game Over ###")
# print("Player 1 score:", player1_score)
# print("Player 2 score:", player2_score)



# import random

# def roll_dice():
#     return random.randint(1, 6)

# def play_game():
#     attempts = 0
#     while attempts < 30:
#         user_input = input("Press Enter to roll the dice, or 'q' to quit: ")
#         if user_input == 'q':
#             print("Thanks for playing!")
#             break
#         else:
#             dice_roll = roll_dice()
#             print("You rolled a", dice_roll)
#             attempts += 1
#     else:
#         print("Maximum attempts reached. Game over.")

# play_game()


import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    target_score = 50
    max_attempts = 30
    player_scores = [0, 0]  # Player 1 score at index 0, Player 2 score at index 1
    attempts = 0

    while attempts < max_attempts:
        current_player = attempts % 2  # Alternates between Player 1 and Player 2
        user_input = input(f"Player {current_player + 1}, press Enter to roll the dice, or 'q' to quit: ")

        if user_input == 'q':
            print("Thanks for playing!")
            break
        else:
            dice_roll = roll_dice()
            player_scores[current_player] += dice_roll
            print(f"Player {current_player + 1} rolled a", dice_roll)
            print(f"Player {current_player + 1} total score:", player_scores[current_player])
            attempts += 1

            if player_scores[current_player] >= target_score:
                print(f"Player {current_player + 1} wins!")
                break
    else:
        print("Maximum attempts reached. Game over.")

play_game()