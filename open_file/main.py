# file = open(file="my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", "w") as file:
    contents = file.read()
    print(contents)