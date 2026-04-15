# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     # for row in data:
#     #     print(row)
#
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from numpy.ma.extras import average

data = pandas.read_csv("weather_data.csv")
#
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# data_list = data["temp"].to_list()
#
# print(average(data_list))
# print(data["temp"].max())
# print(data.temp.max())

# Get row from data table
print(data[data.day == "Monday"])
# Get max temp row
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
fahr = (monday.temp[0] * 9 / 5) + 32
print(fahr)

# Create dataframe from scratch
data_dict = {
    "students" : ["Amy","James", "Angela"],
    "scores" : [76, 56, 65]
}
data2 = pandas.DataFrame(data_dict)
data.to_csv("new_data2.csv")
print(data2)



