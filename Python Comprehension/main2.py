import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data_dict = {letter:code for(letter,code) in data.iterrows()}
print(data_dict)




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

