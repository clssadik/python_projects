import smtplib


my_email = "cillsadik@gmail.com"
password = "lrktocahhgcsipks"

connection = smtplib.SMTP("smtp@gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(
    user=my_email,
    to_addrs="22220030090@mersin.edu.tr",
    msg=f"Subject:Hello\n\nThis is the body of my email."
)
connection.close()
