#Basic stone paper scissors game

import random
user_wins = 0
computer_wins = 0
list_main = ["stone", "paper", "scissors"]

while True:
    user_input = input("Stone/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in list_main:
        continue

    random_number = random.randint(0, 2)
    # stone =0, paper =1, scissors=2 
    computer_pick = list_main[random_number]
    print("Computer picked", computer_pick + ".")

    #user win conditions
    if user_input == "stone" and computer_pick == "scissors":
        print("You won")
        user_wins +=1
        
    elif user_input == "paper" and computer_pick == "stone":
        print("You won")
        user_wins +=1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won")
        user_wins +=1
        
    else:
        print("You lost!")
        computer_wins +=1

print("You won", user_wins,"times.")
print("The computer won", computer_wins, "times.")
print("Goodbye! I hope you had fun.")