import random


choice = ["rock", "paper", "scissors"]
rating_file = open("rating.txt", "r")
rating_from_file = rating_file.readlines()
tmp = []

for line in rating_from_file:
    temp = str.strip(line, '\n')
    tmp.append(temp)

rating_str = " ".join(tmp)

for i in rating_str:




while False:
    counter = 0
    user = input()

    for i in choice:
        if user == i:
            counter = 1

    pc = random.randrange(0, 3)
    pc_choice = choice[pc]

    win = f"Well done. The computer chose {pc_choice} and failed"
    loose = f"Sorry, but the computer chose {pc_choice}"

    if user == "!exit":
        print("Bye!")
        break
    elif counter == 0:
        print("Invalid input")
    elif user == pc_choice:
        print(f"There is a draw ({user})")
    elif user == "rock" and pc_choice == "paper":
        print(loose)
    elif user == "rock" and pc_choice == "scissors":
        print(win)
    elif user == "paper" and pc_choice == "rock":
        print(win)
    elif user == "paper" and pc_choice == "scissors":
        print(loose)
    elif user == "scissors" and pc_choice == "rock":
        print(loose)
    elif user == "scissors" and pc_choice == "paper":
        print(win)


testa

