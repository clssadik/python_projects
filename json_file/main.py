# File not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["fmodjfjns"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")