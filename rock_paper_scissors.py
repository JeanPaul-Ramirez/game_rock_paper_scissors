import random
import asci_rock_paper_scissors


def decision(num):
    if num == 0:
        return asci_rock_paper_scissors.rock
    elif num == 1:
        return asci_rock_paper_scissors.paper
    elif num == 2:
        return asci_rock_paper_scissors.scissors

answer = 0
while answer != 10:
    random_choice = random.randint(0, 2)
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    print(decision(user_choice))
    print("Computer chose:")
    print(decision(random_choice))

    if user_choice == 0 and random_choice == 1:
        print("You lose")
    elif user_choice == 1 and random_choice == 2:
        print("You lose")
    elif user_choice == 2 and random_choice == 0:
        print("You lose")
    elif user_choice == random_choice:
        print("Nobody won")
    else:
        print("You won!")

    answer = int(input("Do you want to play again? If yes -> 5 else 10\n"))


