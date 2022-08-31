#!/usr/bin/env python

"""
# Reading CSV(comma separated values)/tabular data files using CSV library(built-in).
"""
import csv

with open("weather_data.csv") as weather_report:
    data = csv.reader(weather_report)
    #print(data)
    temperature = []
    for row in data:
        #print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
