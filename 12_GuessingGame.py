import random

logo = r"""
  ________                            ___________.__            _______               ___.                 
 /  _____/ __ __   ____   ______ _____\__    ___/|  |__   ____  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |    |   |  |  \_/ __ \ /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  |    |   |   Y  \  ___//    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > |____|   |___|  /\___  >____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                \/     \/        \/            \/    \/     \/       
"""

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
sayi = random.randint(1,100)
print(f"Psssst, the correct answer is {sayi}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
flag = True

while flag:
    if difficulty == "easy":
        attempt = 10
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = input(("Make a guess: "))
