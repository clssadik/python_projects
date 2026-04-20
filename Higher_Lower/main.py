import art
from game_data import data
import random

print(art.logo)

flag = True
score = 0

def truestate(get_score):
    print("\n" * 20)
    print(art.logo)
    print(f"You're right! Current score {get_score}")

def falsestate(get_score):
    print("\n" * 20)
    print(art.logo)
    print(f"Sorry, that's wrong. Final score {get_score}")

s1 = random.randint(0, len(data) - 1)
while flag:
    s2 = random.randint(0, len(data) - 1)
    while s1 == s2:
        s2 = random.randint(0, len(data) - 1)

    followersA = data[s1]['follower_count']
    followersB = data[s2]['follower_count']
    print(f"Compare A: {data[s1]['name']}, a {data[s1]['description']}, from {data[s1]['country']} ")
    print(art.vs)
    print(f"Compare B: {data[s2]['name']}, a {data[s2]['description']}, from {data[s2]['country']} ")
    try:
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if choice not in ['A', 'B']:
            raise ValueError("Invalid letter entered")

        if choice == 'A':
            if followersA >= followersB:
                score += 1
                truestate(score)
                s1 = s2
            else:
                falsestate(score)
                flag = False

        elif choice == 'B':
            if followersB >= followersA:
                score += 1
                truestate(score)
                s1 = s2
            else:
                falsestate(score)
                flag = False

    except ValueError:
        print("\nInvalid input! Please type only 'A' or 'B'.")
        continue