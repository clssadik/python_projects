#File not found
import os
os.chdir(os.path.dirname(__file__)) 

try:
    file = open("a_file.txt")
    my_dict = {"key": "value"}
    # print(my_dict["msdfmjsdfj"])
    print(my_dict["key"])
except FileNotFoundError:
    file  = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"key does not exist {error_msg}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    # print("File was closed.")
    raise KeyError