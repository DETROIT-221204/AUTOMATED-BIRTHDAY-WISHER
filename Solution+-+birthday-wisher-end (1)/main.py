
my_email=""#YOUR EMAIL
password=""# ON CGROME TYPE APP PASSWORD AND GENERATE A PASSWORD
import smtplib
import datetime as dt
import pandas
import random
taday=dt.datetime.now()
today_tuple=(taday.month,taday.day)
data=pandas.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates\\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
birthday_person=birthdays_dict[today_tuple]
to_addr=birthday_person["email"]
connection.sendmail(from_addr=my_email,to_addrs=to_addr,msg=f"Subject:Happy Birthday\n\n{contents}")
connection.close()