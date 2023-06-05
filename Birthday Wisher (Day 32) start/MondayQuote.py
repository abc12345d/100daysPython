import datetime as dt
import smtplib
import random

MY_EMAIL = 'jeanli9753@gmail.com'
PASSWORD = 'hrbusnyqgacpuuiw'

now = dt.datetime.now()
weekday = now.weekday()

# only send quote on Mondays
if weekday == 0:
    with open('./quotes.txt','r') as file:
        quote_list = file.readlines()
        quote = random.choice(quote_list)
        print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = 'jeanli9753@yahoo.com',
            msg = f'Subject:Quote for Monday~\n\n{quote}' 
        )

