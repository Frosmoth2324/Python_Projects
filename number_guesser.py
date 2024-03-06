import random
MIN_NUM = 0
MAX_NUM = 31
TURNS = 5

def main():
    num = random.randint(MIN_NUM, MAX_NUM)
    win = False
    for i in range(TURNS):
        print(f"Pick a number between {MIN_NUM} and {MAX_NUM-1}")
        guess = input()
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Your deposit must be a whole number")
        if guess == num:
            print("You are correct!")
            win = True
            break
        elif guess < num:
            print("Higher")
        elif guess > num:
            print("lower")
        else:
            print("Error, var num not acceptable value")
    if win == True:
        print("You Won!")
        exit()
    else:
        print("Sorry you lost")
        exit()


while True:
    main()