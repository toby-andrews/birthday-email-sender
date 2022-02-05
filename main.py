import random
import smtplib
import datetime as dt
import pandas as pd

# read the birthdays cv and save to variable

data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

# open the three letter templates and save to a list (IS THERE A BETTER WAY?)

letters = []

with open("./letter_templates/letter_1.txt") as file:
    letter1 = file.read()
    letters.append(letter1)

with open("./letter_templates/letter_2.txt") as file2:
    letter2 = file2.read()
    letters.append(letter2)

with open("./letter_templates/letter_3.txt") as file3:
    letter3 = file3.read()
    letters.append(letter3)

# Get the day and month it is today

now = dt.datetime.now()
today_day = now.day
today_month = now.month


# This is the last function called, but above the for loop it as requires the input from it.
# Randomly picks a template, takes name from birthdays and replaces it in the template
# Sends the email to the email given in the function

def write_email(name, email):
    global letters
    chosen_template = random.choice(letters)
    birthday_letter = chosen_template.replace("[NAME]", (name.strip()))
    my_email = "testtesttest@gmail.com"
    password = "testestes"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{birthday_letter}")


# This for loop goes through the dictionary and gets the day and month value then compares against today's
# If it is match it pulls the name and email and calls to write email function

for x in birthdays:
    day = (x["day"])
    month = (x["month"])
    if month == today_month and day == today_day:
        name = (x["name"])
        email = (x["email"])
        write_email(name, email)
