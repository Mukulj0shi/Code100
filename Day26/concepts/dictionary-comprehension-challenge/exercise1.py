#!usr/env/bin python

"""
Exercise 1:
Use Dictionary comprehension to create a dictionary called result that takes
each word in the given sentence and calculates the number of letters in each word
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_words = sentence.split()
print(list_words)

# word_dictionary = {key: value for item in list_words}   >>> here we have to define key as item which iterate through the list.
word_dictionary = {word: len(word) for word in list_words}
print(word_dictionary)

"""
Exercise 2:
Use Dictionary comprehension to create a dictionary that takes each temperature in celsius and convert it into Farenheight.
"""

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# new_weather_f = {key: value for (key,value) in weather_c.items()}   >>> here we have to define key as day and value as temp
# which iterate through the dictionary.
new_weather_f = {day: ((temp * 9 / 5) + 32) for (day, temp) in weather_c.items()}
print(new_weather_f)
