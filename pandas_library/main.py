import pandas

# create a dataframe from scratch
data_dict2 = {
    "students" : ["Amy","James","Angela"],
    "scores" : [76,56,65]
}
data2 = pandas.DataFrame(data_dict2)
print(data2)


data = pandas.read_csv("weather_data.csv")
print(type(data.day))
print(data)

data_dict = data.to_dict()

temp_list = data.temp.tolist()

# average temparature
print(sum(temp_list) / len(temp_list) )

# get data in rows ***
print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# fahr = monday.temp[0]*9/5 + 32
# print(fahr)


