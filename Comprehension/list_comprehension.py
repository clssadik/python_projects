# List comprehension
# new_list = [n for n in list]

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

new_list = [n*n for n in range(1,5)]
print(new_list)

names = ["Alex","Beth","Caroline","Elanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)