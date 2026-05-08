# import smtplib


# my_email = "cillsadik@gmail.com"
# password = "lrktocahhgcsipka"

# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="22220030090@mersin.edu.tr",
#         msg=f"Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2002,month=9,day=27)
print()