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

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(4)
except IndexError:
    print("Fruit pie")


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
        try:
            total_likes = total_likes + post['Likes']
        except:
            pass
    
    return total_likes


count_likes(facebook_posts)
