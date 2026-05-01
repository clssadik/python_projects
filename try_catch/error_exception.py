import pandas

data = pandas.read_csv("/Users/clssadik/Documents/python_projects/try_catch/nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    try:
        answer = input("Enter a word: ").upper()
        new_list = [data_dict[letter] for letter in answer]
        print(new_list)
        break
    except KeyError:
        print("Please enter a valid word.")
    # new_list = [n for n in list]
