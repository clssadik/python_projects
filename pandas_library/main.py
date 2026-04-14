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

# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
data_list = data["temp"].to_list()
print(data_list)
print(average(data_list))