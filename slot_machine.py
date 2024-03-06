import random

ROWS = 3
COLS = 3


MAX_LINES = ROWS
MAX_BET = 100
MIN_BET = 1




symbol_count = {
    "A": 4,
    "B": 8,
    "C": 10,
    "D": 14
}

symbol_value = {
    "A": 100,
    "B": 25,
    "C": 16,
    "D": 9
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()



def deposit():
    while True:
        amount = input("Please enter the amount of money you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Your deposit must be greater than 0")
        else:
            print("Your deposit must be a whole number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines you want to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("You can only bet on 1 to " + str(MAX_LINES) + " lines")
        else:
            print("The number of lines you bet on has to be a number")
    return lines

def get_bet():
    while True:
        amount = input("Please enter the amount of money you want to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Your bet must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Your bet must be a whole number")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} line(s). This means you are betting ${total_bet} in total.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on line(s):", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is: ${balance}")
        answer = input("Press enter to play or q to quit:")
        if answer == "q":
            break
        balance += spin(balance)
        if balance == 0:
            break
    
    if balance == 0:
        print("You're bust!")
    else:
        print(f"You left with ${balance}")


while True:
    main()
    play = input("Press enter to play again or q to quit:")
    if play == "q":
        break