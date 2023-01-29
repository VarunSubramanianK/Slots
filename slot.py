import random

MAX_LINES = 3 ## Constant global variables 
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count={
    "$":2,
    "#":4,
    "%":6,
    "*":8
}

values={    
    "$":5,
    "#":4,
    "%":3,
    "*":2
}           ## Multiplier values when won

def check_winnings(coloums,lines,bet,values):
    winings=0
    wining_lines=[]
    for line in range(lines):
        symbol = coloums[0][line]
        for coloum in coloums:
            symbol_check = coloum[line]
            if symbol != symbol_check:
                break
        else:                                   ## This else is for the 'for loop' this will be excuted if the for look doesn't break from the previous 'if statement'
            winings+=values[symbol]*bet
            wining_lines.append(line+1)        ## 'line' in this function is counting the index. so plus 1 is needed to get the actual line bet on.
            
    return winings, wining_lines
            
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():  ## .item() - gives you the value associated with both the key and item in one go
        for _ in range(symbol_count):   ## "_" - we use it when don't care about the iteration value (anonymos variable)
            all_symbols.append(symbol)
    coloums=[]
    for _ in range(cols):
        coloum=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            coloum.append(value)
        coloums.append(coloum)
    return coloums

def print_slot_machine(coloums):
    for row in range(len(coloums[0])):
        for i,coloum in enumerate(coloums): ## enumerate - gived both the index and the value
            if i != len(coloums)-1:
                print(coloum[row], end=" | ") ## end - defines what to do after completing the print statement. it is default to '/n'
            else:
                print(coloum[row], end="")
        print()
                
                
    

def deposite():
    while True:
        
        amount=input("Enter the Deposite amount: ")
        if amount.isdigit():
            amount=int(amount)
            if amount<0:
                print("Enter a positive integer")
            else:
                break
        else:
            print("Please enter a valid Number")
    return amount 

def get_number_of_lines():
    while True:
        lines=input("Enter the required number of lines from (1 to %s): "% MAX_LINES)
        if lines.isdigit():
            lines=int(lines)
            if lines <1 or lines >3:
                print("Enter a number between 1 and 3")
            else:
                break
        else:
            print("Please enter a valid Number")
    return lines 

def get_bet():
    while True:
        bet=input("Enter the Bet amount on each line: ")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Enter a bet between {MIN_BET} and {MAX_BET}") ##Another way of printing variables (using f)
        else:
            print("Please enter a valid Number")
    return bet
    

def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"Insuficiant amount in Balance. Balance: {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet: {total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winings,winings_line=check_winnings(slots,lines,bet,values)
    print(f"You have won: {winings}")
    print(f"You have won on the lines: ",*winings_line)        ## this '*' - splash operater, unpacks the variable line by line
    return winings-total_bet
    
def main():
    balance=deposite()
    while True:
        print(f"Current balance is {balance}")
        ans=input("Press enter to play (q to quit).")
        if ans=='q':
            break
        balance+=spin(balance)
    print(f"You are left with {balance}")
    
    
    
main()
