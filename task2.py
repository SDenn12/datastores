# Task 2
from datetime import date

name = input("What is your name? ")
age = int(input("How old are you? "))

current = date.today().year


birthday = input("When was your birthday? Format as MM-DD")
birthday = birthday.split("-")
birthyear = 0

if date.today().month > int(birthday[0]):
    birthday_yet = True

elif date.today().month == int(birthday[0]):
    if date.today().day >= int(birthday[1]):
        birthday_yet = True
    else:
        birthday_yet = False

elif date.today().month < int(birthday[0]):
    birthday_yet = False

else:
    print("That was not a valid birthday")


if birthday_yet:
    birthyear = current-age
else:
    birthyear = current-age-1

print(f"OMG {name}, you are so old you were born in {birthyear}")
