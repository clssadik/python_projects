name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_range = [n*2 for n in range(1,5)]
print(new_range)

names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
short_names = [name for name in names if len(name)<5]
print(short_names)