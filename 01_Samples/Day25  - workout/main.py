# with open("weather_data.csv") as wdata:
#     data = wdata.readlines()
#
# print(data)
#
# import csv
#
# with open("weather_data.csv") as w_data:
#     data = csv.reader(w_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) # data frame
# print(data["temp"]) # series
# data_dict = data.to_dict()
# print(data_dict)
# temperatures = data["temp"].to_list()
# average = round(sum(temperatures)/len(temperatures),2)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in columns
# print(data.condition)

# get row from a dataframe
# print(data[data.day == "Friday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temperature = (monday.temp * 9 /5) + 32
# print(temperature)

# dataframe from scratch
# family = {
#     "names": ["Ranga", "Sneha", "Skandan", "Charu"],
#     "age": [42, 40, 12, 68]
# }
# data = pandas.DataFrame(family)
# data.to_csv("family.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].to_list()
grey = 0
black = 0
cinnamon = 0
for color in fur_color:
    if color == "Gray":
        grey += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

squirrel_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, cinnamon, black]
}
pandas.DataFrame(squirrel_data).to_csv("squirrel_count.csv")



