import random

logo = r"""
  ________                            ___________.__            _______               ___.                 
 /  _____/ __ __   ____   ______ _____\__    ___/|  |__   ____  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |    |   |  |  \_/ __ \ /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  |    |   |   Y  \  ___//    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > |____|   |___|  /\___  >____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                \/     \/        \/            \/    \/     \/       
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
sayi = random.randint(1,100)
print(f"Psssst, the correct answer is {sayi}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
flag = True

def logic(guess):
    global sayi
    if guess < sayi:
        print("Too low.")
    elif guess > sayi:
        print("Too high.")
    elif guess == sayi:
        print(f"You got it! The answer was {guess}")
        return 0

def while_loop(attempt):
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input(("Make a guess: ")))
        logic(guess)
        print("Guess again.")
        attempt -= 1
    if attempt == 0:
        print("You've run out of guesses, you lose.")
        return 0

while flag:
    if difficulty == "easy":
        attempt = 10
        while_loop(attempt)
        flag = False
    elif difficulty == "hard":
        attempt = 5
        while_loop(attempt)
        flag = False
