# !usr/bin/env python3
import re

with open("file1.txt") as file1:
    list1 = file1.readlines()  # Create a list of items in the file

with open("file2.txt") as file2:
    list2 = file2.readlines()

    newlist3 = []
    newlist3 = [int(number.rstrip())     for number in list2 if number in list1 and number not in newlist3]
    print(newlist3)
