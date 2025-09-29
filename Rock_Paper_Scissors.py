import random

user_wins = 0
computer_wins = 0
is_a_tie = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor Or 'Q' To Quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Please Enter A Valid Option.")
        continue
    
    random_number = random.randint(0, 2)
    #rock:0, paper:1, scissor:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's A Tie!")
        is_a_tie += 1
    else:
        print("You Lost!")
        computer_wins += 1

print("You Won", user_wins, "Times.")    
print("The Computer Won", computer_wins, "Times.")
print("There Were", is_a_tie, "Ties.")
print("Exiting The Game...")
print("See Ya!")