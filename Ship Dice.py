import random

def roll_dice(num_dice):
    result = []
    for i in range(num_dice):
        result.append(random.randint(1, 6))
    return result

print('Welcome to Ship Dice Game')
print('-------------------------')
print('rules = "Each player rolls six dice. They need a ‘ship’ (6), a ‘captain’ (1) and crew. If they have a ship and captain in their roll, their crew (score) is the sum of all the other dice. If they do not have a ship and captain they can roll again, keeping a ‘ship’ if they have one and only rolling five dice. If on their second roll they still have no ship and captain their score is 0. The highest score wins')

num_players = 0

while True:
    
    num_players = input("Welcome to the game, how many players are there? (1-4):")

    try:
        
        num_players = int(num_players)
        
        if num_players > 0 and num_players <= 4:
            break
        else:
            print("Please enter only 1 to 4 players!")

    except Exception as e:
        
        print("Please enter an integer value.")



scores = [0] * num_players
current_player = 0


while True:

    
    turn_score = 0
    turn_rolls = roll_dice(6)

    
    if 1 in turn_rolls and 6 in turn_rolls:
        turn_rolls.pop(turn_rolls.index(1))
        turn_rolls.pop(turn_rolls.index(6))
        turn_score = sum(turn_rolls)

    
    elif 6 in turn_rolls:
        turn_rolls = roll_dice(5)
        if 1 in turn_rolls:
            turn_rolls.pop(turn_rolls.index(1))
            turn_score = sum(turn_rolls)

    
    else:
        turn_rolls = roll_dice(6)
        if 1 in turn_rolls and 6 in turn_rolls:
            turn_rolls.pop(turn_rolls.index(1))
            turn_rolls.pop(turn_rolls.index(6))
            turn_score = sum(turn_rolls)

    print("Player", current_player, "scored", turn_score)
    scores[current_player] = turn_score

    current_player += 1

    
    if current_player - 1 == num_players - 1:
        winner = scores.index(max(scores))
        print("Player", winner, "won!")

        play_again = input("Would you like to play again? (y/n)")
        if play_again == 'y':
            scores = [0] * num_players
            current_player = 0
        else:
            print("Bye. See you later.....")
            break
