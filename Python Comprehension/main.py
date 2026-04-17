name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_range = [n*2 for n in range(1,5)]
print(new_range)

names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
short_names = [name for name in names if len(name)<5]
print(short_names)

upper_case_names = [name.upper() for name in names if len(name)>5]
print(upper_case_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2 == 0]
print(result)

with open("file1.txt") as d1:
    list1 = d1.read().splitlines()

with open("file2.txt") as d2:
    list2 = d2.read().splitlines()

result = [int(num) for num in list1 if num in list2]

print(result)

# .readlines() -> Çıktısı: ['1\n', '2\n', '3']
# .splitlines() -> Çıktısı: ['1', '2', '3']