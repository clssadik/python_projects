logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

user_data = {}
def logic():
        name = input("What is your name? ")
        teklif = int(input("What is your bid?: $"))
        user_data[name] = teklif


logic()
kontrol = True

while kontrol:
    choice = input("Are there any other bidders? Type 'yes' or 'no': ")
    if choice == "yes":
        print("\n" * 100)
        logic()
    else:
        kontrol = False
        temp1 = 0
        temp2 = ""
        for letter in user_data:
            if user_data[letter] > temp1:
                temp1 = user_data[letter]
                temp2 = letter
        print(f"The winner is {temp2} with a bid of ${temp1}")
