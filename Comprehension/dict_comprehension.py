# New Dict
# new_dict = {key:value for (key,value) in dict.items() if test}

import pandas
import random


names = ["Alex","Beth","Caroline","Elanor","Freddie"]
std_score = {name:random.randint(1,100) for name in names}
passed_students = {name:score for (name,score) in std_score.items() if score >= 60}
print(passed_students)