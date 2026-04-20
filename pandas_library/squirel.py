import pandas

data = pandas.read_csv("sq.csv")
black = len( data[data["Primary Fur Color"] == "Black"] )
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])

new_dict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count" : [gray, red, black],
}

dataframe = pandas.DataFrame(new_dict)
dataframe.to_csv("squirrel.csv")
