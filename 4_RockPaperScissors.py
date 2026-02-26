import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
liste = [rock,paper,scissors]
print("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
choice = int ( input() )
computer = random.randint(0,2)

print("You chose")
print(liste[choice])
print("Computer chose")
print(liste[computer])

if choice == computer:
    print("Draw")
elif choice == 0 and computer == 1 :
    print("You lose!")
elif choice == 0 and computer == 2 :
    print("You win!")
elif choice == 1 and computer == 0 :
    print("You win!")
elif choice == 1 and computer == 2 :
    print("You lose!")
elif choice == 2 and computer == 0 :
    print("You lose!")
elif choice == 2 and computer == 1 :
    print("You win!")

