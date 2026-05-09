##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random

now = dt.datetime.now()
month = now.month
day = now.day
random_int = random.randint(1,3)
print(random_int)

data_file = pandas.read_csv("birthdays.csv")

# if month == data_file["month"][0] and day == ["day"][0]:


print(day)

