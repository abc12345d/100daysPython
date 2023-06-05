##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import os
import random
import smtplib

MY_EMAIL = 'jeanli9753@gmail.com'
PASSWORD = 'hrbusnyqgacpuuiw'

birthdays_df = pd.read_csv('birthdays.csv')
now = dt.datetime.now()

# 2. today birthday star if today matches a birthday in the birthdays.csv
birthday_star = birthdays_df.loc[(birthdays_df.month == now.month) & (birthdays_df.day == now.day)]

if not birthday_star.empty:
    # 3a. pick a random letter from letter templates
    letters_dir = 'letter_templates/'
    letter_file = random.choice(os.listdir(letters_dir))

    with open(f'{letters_dir}{letter_file}','r') as file:
        letter = file.read()

    # 3b. replace the [NAME] with the person's actual name from birthdays.csv
    letter = letter.replace('[NAME]', birthday_star.name.to_string(index= False))

    # 4. send email
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= birthday_star.email.to_string(index= False),
            msg= f'Subject:Love for your big day!\n\n{letter}'
        )