import random


user_wins=0
com_wins=0
draw=0
options=["rock","paper","scissors"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to Quit:").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    com_pick=options[random_number]
    print("Computer picked",com_pick + ".")

    if user_input == "rock" and com_pick=="scissors":
        print("You Won!")
        user_wins+=1

    elif user_input == "paper" and com_pick == "rock":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and com_pick == "paper":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and com_pick == "scissors":
        print("Match Draw!")
        draw += 1
    elif user_input == "paper" and com_pick == "paper":
        print("Match Draw!")
        draw += 1
    elif user_input == "rock" and com_pick == "rock":
        print("Match Draw!")
        draw += 1

    else:
        print("You Lost!")
        com_wins+=1

print("You Won",user_wins,"times !!!")
print("You Lost",com_wins,"times!!!")
print("Match Drawn",draw,"times!!!")
print("Goodbye!")