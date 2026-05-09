import smtplib
import datetime as dt


my_email = "cillsadik@gmail.com"
password = "lrktocahhgcsipks"

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as file:
    array = [satir.strip() for satir in file]

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="22220030090@mersin.edu.tr",
        msg=f"Subject:Hello\n\n{array[day_of_week]}".encode("utf-8")
    )