# Three ways to handle csv file in python:

# 1 . without any library
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# 2. with python built-in csv library
# import csv
# with open("weather_data.csv") as data_file:
#     # data is a 2d array in the underlying
#     data = csv.reader(data_file)
#     next(data)
#     temperature = []
#     for row in data:
#         temperature.append(int(row[1]))
#     print(temperature)

# 3. with pandas library
import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])