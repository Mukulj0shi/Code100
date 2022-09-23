from datetime import datetime
import random
import smtplib

sender_email = "mukultest100@gmail.com"
password_user = "Python@123"
current_time = datetime.now()

if current_time.weekday() == 3:
    with open("quotes.txt", "r") as quotes:
        today_quote = (random.choices(quotes.readlines()))[0].rstrip()
        # print(today_quote)

        # Send above quote to sender
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=sender_email, password=password_user)
        connection.sendmail(from_addr=sender_email,
                            to_addrs="mukujosh@gmail.com",
                            msg=f"Subject:Motivation quote\n\n{today_quote}")
        connection.close()
