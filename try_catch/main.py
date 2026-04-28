# #File not found
# import os
# os.chdir(os.path.dirname(__file__)) 

# try:
#     file = open("a_file.txt")
#     my_dict = {"key": "value"}
#     # print(my_dict["msdfmjsdfj"])
#     print(my_dict["key"])
# except FileNotFoundError:
#     file  = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"key does not exist {error_msg}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     # print("File was closed.")
#     raise KeyError

# height = float(input("Height : "))
# weight = int(input("Weight : "))

# if height > 3:
#     raise ValueError("Human height should not be above 3 meters")

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try: 
    make_pie(4)
except IndexError:
    print(f"Fruit Pie")



facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        total_likes = total_likes + post['Likes']
    
    return total_likes


try:
    count_likes(facebook_posts)
except KeyError:
    print("Key Error")