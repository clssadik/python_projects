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
