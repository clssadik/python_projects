# File not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # Different type of error
    print(a_dictionary["fmodjfjns"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")