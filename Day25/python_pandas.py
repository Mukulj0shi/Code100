#!/usr/bin/env python

"""
# Reading CSV(comma separated values) data files using panda library
# It is a powerful tool to perform data analysis on tabular data.
# csv file is read using read_csv while tabluar data is read using read_table
"""
import pandas

# read_csv() function is used to read excel as a dataframe object.
weather_data = pandas.read_csv("weather_data.csv")
print(weather_data)

# Complete sheet is a dataframe object in pandas.
# print(type(weather_data))

# One column is referred as data series object in pandas. To get series from data frame.
# print(type(weather_data["temp"]))


# Using pandas conversion methods to convert the dataframe to a list.
# https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html
data_list = weather_data["temp"].to_list()
print(data_list)

# Using pandas conversion methods to convert the dataseries to a dictionary.
data_dictionary = weather_data.to_dict()
print(data_dictionary)

# Using list comprehensions
n = 0
total_temp = [n := x + n for x in data_list][-1]
avg_temp = total_temp / len(data_list)
print(avg_temp)

# Using dataseries methods available from pandas library. Format ==> data_series.method_name()
average_temp = weather_data["temp"].mean()
print(average_temp)

# Using max dataseries method available from pandas library. Format ==> data_series.method_name()
max_temp = weather_data["temp"].max()
print(max_temp)

# Obtaining information from a column, based on some value in that column.
# When row value is equivalent to a value in the column. Format ==> Dataseries[dataseries.columnname == "value of column"]
print(weather_data[weather_data.day == "Monday"])

maximum_temp = weather_data[weather_data.temp == weather_data["temp"].max()]
print(maximum_temp)

column_monday = weather_data[weather_data.day == "Monday"]
degree_t_farenheit = ((int(column_monday.temp))*9/5) + 32
print(degree_t_farenheit)

# Creating a dataframe from scratch using pandas. Format ==> pandas.DataFrame(dictionary_name)
my_dict = dict(Vendor=["Cisco", "Juniper", "Arista"], Device=["N9322D", "SRX", "EOS"])
my_dataframe = pandas.DataFrame(my_dict)

# Creating a CSV file from the above given dataframe values.
my_dataframe.to_csv("created_from_dataframe.csv")
print(my_dataframe)

