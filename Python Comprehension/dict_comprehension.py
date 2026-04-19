# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()

names = ["Alex","Beth","Caroline","Dave","Elanor","Freddie"]
import random
students_score = {student:random.randint(1,100) for student in names}
print(students_score)
passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students)

# bir cümleyi liste haline getirip, listeyi kullanarak dictionary kurmak
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {sent:len(sent) for sent in sentence_list}
print(result)

# celciustan fahrenheit'a çevirdim"
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(celc*9/5)+32 for (day,celc) in weather_c.items()}
print(weather_f)