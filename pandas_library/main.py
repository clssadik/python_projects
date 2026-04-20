import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data.day))
print(data)

data_dict = data.to_dict()

temp_list = data.temp.tolist()

# average temparature
print(sum(temp_list) / len(temp_list) )

# get data in rows ***
print(data[data.temp == data.temp.max()])
