#FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    # print(a_dictionary["dfdfıjkısd"])
    print(a_dictionary["key"])


# I should never use a bare except block without specifying an exception type.
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
# try bloğundan sonra eğer except içerisine girmediyse else triggerlanır
else:
    content = file.read()
    print(content)
finally:
    file.close()
    # Raising my own exceptions
    # raise KeyError("uydurdum")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height shouldn't be over 3 meters")

bmi = weight / height ** 2
print(bmi)


