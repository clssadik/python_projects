# file = open(file="my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("/Users/clssadik/Pictures/my_file.txt",mode="w") as file:
    file.write("hello world")
