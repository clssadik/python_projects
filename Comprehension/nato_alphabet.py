#TODO 1. Create a dictionary in this format: { "A": "Alfa","B": "Bravo" }
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

answer = input("Enter a word: ").upper()
# new_list = [n for n in list]
new_list = [data_dict[letter] for letter in answer]
print(new_list)

