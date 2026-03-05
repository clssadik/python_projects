logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
flag = True

def add():
    user = []
    user.append(random.choice(cards))
    user.append(random.choice(cards))
    return user

def add_computer():
    computer = []
    computer.append(random.choice(cards))
    computer.append(random.choice(cards))
    return computer

def one_add():
    once = []
    once.append(random.choice(cards))
    return once[0]

def logic(s1,s2):
    if s1 > 21 and s2 > 21:
        print("You lose 😤")
    elif s1 > 21 and s2 <= 21:
        print("You lose 😤")
    elif s1 <= 21 and s2 > 21:
        print("Oppenent went over. You win 😁")
    elif s1 <= 21 and s2 <= 21:
        if s1 > s2:
            print("You win 😁")
        elif s1 == s2:
            print("Draw 🙃")
        else:
            print("You lose 😤")


while flag:
    choice1 = input("Dou you want to play a game of BlackJack? Type 'y' or 'n': ")
    if choice1 == "y":
        print("\n" * 20)
        print(logo)
        returned_user = add()
        print(f"Your cards: {returned_user}, current score: {sum(returned_user)}")
        returned_computer = add_computer()
        print(f"Computer's first card: {returned_computer[0]}")
        choice2 = input("Type 'y' to get another card or type 'n' to pass: ")
        flag2 = True
        while flag2:
            if choice2 == "y":
                new_user = one_add()
                returned_user.append(new_user)
                print(f"Your cards: {returned_user}, current score: {sum(returned_user)}")
                print(f"Computer's first card: {returned_computer[0]}")
                if sum(returned_user) > 21:
                    flag2 = False
                else:
                    choice2 = input("Type 'y' to get another card or type 'n' to pass: ")
            elif choice2 == "n":
                flag2 = False
        print(f"Your final hand: {returned_user}, final score: {sum(returned_user)}")
        while sum(returned_computer) < 17:
            new_computer = one_add()
            returned_computer.append(new_computer)
        print(f"Computer's final hand: {returned_computer}, final score: {sum(returned_computer)}")
        s1 = sum(returned_user)
        s2 = sum(returned_computer)
        logic(s1, s2)

    else:
        flag = False


