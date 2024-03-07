import random
MAX_SCORE = int(input("How many points are you playing untill:"))
score1 = 0
score2 = 0
player = 1

def player1():
    print("Player 1 up")
    round_score1 = 0
    while True:
        play = input("Press the return key to roll or q to end your turn")
        if play == "q":
            break
        roll_value = random.randint(1,6)
        print(f"You rolled a {roll_value}")
        if roll_value == 1:
            print("Turn over")
            round_score1 = 0
            break
        else: 
            round_score1 += roll_value
            print(f"Your round score is: {round_score1}")
    return round_score1

def player2():
    print("Player 2 up")
    round_score2 = 0
    while True:
        play = input("Press the return key to roll or q to end your turn")
        if play == "q":
            break
        roll_value = random.randint(1,6)
        print(f"You rolled a {roll_value}")
        if roll_value == 1:
            print("Turn over")
            round_score2 = 0
            break
        else: 
            round_score2 += roll_value
            print(f"Your round score is: {round_score2}")
    return round_score2

while score1 < MAX_SCORE or score2 < MAX_SCORE:
    round_score1 = player1()
    score1 += round_score1
    print(f"Your current score is: {score1}")
    round_score2 = player2()
    score2 += round_score2
    print(f"Your current score is: {score2}")
    if score1 == score2:
        winner = 3
    elif score1 >= MAX_SCORE:
        winner = 1
    elif score2 >= MAX_SCORE:
        winner = 2
if winner == 1:
    print("Player 1 Won")
elif winner == 2:
    print("Player 2 Won")
elif winner == 3:
    print("It's A Tie!")