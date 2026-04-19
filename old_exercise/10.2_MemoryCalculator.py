logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add
    ,"-" : subtract
    , "*" : multiply
    , "/" : divide
}

flag = True
s1 = 0.0
s2 = 0.0
ch = ""

first_number = float(input("What is your first number? "))

def logic(first_number):
    global s1, s2, ch
    s1 = first_number
    for i in operations:
        print(f"{i}")
    choice = input("Pick an operation: ")
    ch = choice
    second_number = float(input("What is the next number? "))
    s2 = second_number
    result = operations[choice](first_number, second_number)
    return result

while flag:
    result_returned = logic(first_number)
    print(f"{s1} {ch} {s2} = {result_returned}")
    should_continue = input(f"Type 'y' to continue calculating with {result_returned}, or type 'n' to start a new calculation: ")
    if should_continue == "y":
        first_number = result_returned
    else:
        print()
        first_number = float(input("What is your first number? "))