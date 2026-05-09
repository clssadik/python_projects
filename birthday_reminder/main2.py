##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib

my_email = "cillsadik@gmail.com"
password = "lrktocahhgcsipks"

now = dt.datetime.now()
month = now.month
day = now.day

data_file = pandas.read_csv("birthdays.csv")


if month == data_file["month"][0] and day == data_file["day"][0]:
    
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        
        data = file.read()
        name_changed = data.replace("[NAME]", data_file["name"][0])
        
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data_file["email"][0],
                msg=f"Subject:Happy Birthday\n\n{name_changed}".encode("utf-8")
            )

