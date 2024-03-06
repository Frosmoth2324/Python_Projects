CLEAR_AND_RETURN = "\33[H"




def main():
    score = 0
    print("Welcome to the quiz game!")
    print("Lets begin!")
    print("What is love?")
    answer = input()
    if answer.lower() == "baby don't hurt me":
        print("Correct!")
        score += 1
        print(f"Your score is: {score}")
    else:
        print("Sorry, the correct answer was:")
        print("baby don't hurt me")
        print(f"Your score is: {score}")
    print("What does CPU stand for?")
    answer = input()
    if answer.lower() == "central prossesing unit":
        print("Correct!")
        score += 1
        print(f"Your score is: {score}")
    else:
        print("Sorry, the correct answer was:")
        print("central prossesing unit")
        print(f"Your score is: {score}")

main()
