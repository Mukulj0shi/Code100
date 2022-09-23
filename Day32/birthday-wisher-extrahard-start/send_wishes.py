from datetime import datetime
import pandas as pd
import random
import smtplib

current_date = datetime.now()
now_year = current_date.year
now_month = current_date.month
now_date = current_date.day
sender_email = "mukultest100@gmail.com"
password_user = "Python@123"
list_of_file = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# Choose one of the letter in a random fashion
wish_card = random.choice(list_of_file)


with open("birthdays.csv", "r") as birthday_data:
    bd = pd.read_csv(birthday_data)
    # Read data in the form of list with column:index in the form of a key:value pair of dictionary.
    name_birthday = bd.to_dict("records")
    #print(name_birthday)
    for item in range (0, len(name_birthday)-1):
        if name_birthday[item]["month"] == now_month and name_birthday[item]["day"] == now_date:
            with open(wish_card) as bday_line:
                line_list = bday_line.readlines()
                # Change name in the first line to the name of bday person
                first_line = line_list[0].rstrip().split(" ")
                first_line[1] = name_birthday[item]["name"]
                # Create a string from the first line
                line_list[0] = " ".join(first_line)
                print(line_list)
                # Create bday wish in the form of a string from the list using join() method.
                bday_wish = " ".join(line_list)
                print(bday_wish)
                email_bdayguy = name_birthday[item]["email"]
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user=sender_email, password=password_user)
                connection.sendmail(from_addr=sender_email,
                                    to_addrs=email_bdayguy,
                                    msg=f"Subject:Motivation quote\n\n{bday_wish}")
                connection.close()
