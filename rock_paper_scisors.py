import random

COMP_CHOICE = ["r", "p", "s"]

user_wins = 0
comp_wins = 0

while True:
    comp_input = random.choice(COMP_CHOICE)
    print("Rock, Paper, Scissors or Quit")
    user_input = input("[r/p/s/q]")
    if user_input == "q":
        exit()
    else:
        if comp_input == "s" and user_input == "r":
            print("You won")
            user_wins += 1
        elif comp_input == "r" and user_input == "p":
            print("You won!")
            user_wins += 1
        elif comp_input == "p" and user_input == "s":
            print("You won!")
            user_wins += 1
        elif comp_input == "r" and user_input == "s":
            print("You lost!")
            comp_wins += 1
        elif comp_input == "p" and user_input == "r":
            print("You lost!")
            comp_wins += 1
        elif comp_input == "s" and user_input == "p":
            print("You lost!")
            comp_wins += 1
        elif comp_input == "r" and user_input == "r":
            print("Tie")
        elif comp_input == "p" and user_input == "p":
            print("Tie")
        elif comp_input == "s" and user_input == "s":
            print("Tie")
        
        
        if comp_input == "s":
            print("The computor got scissors")
        elif comp_input == "p":
            print("The computor got paper")
        elif comp_input == "r":
            print("The computor got rock")
        
        
        if comp_wins > user_wins:
            print(f"You are losing {comp_wins} to {user_wins}")
        elif comp_wins < user_wins:
            print(f"You are winning {user_wins} to {comp_wins}")