import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = 'jeanli9753@gmail.com'
PASSWORD = 'hrbusnyqgacpuuiw'
MY_LAT = 51.493179
MY_LONG = 0.067800

def is_night():
    api_parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params= api_parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_hour = int(sunrise.split('T')[1].split('+')[0].split(':')[0])
    sunset_hour = int(sunset.split('T')[1].split('+')[0].split(':')[0])

    current_hour = datetime.now().time().hour

    if current_hour < sunrise_hour or current_hour > sunset_hour:
    # if sunrise_hour <= current_hour <= sunset_hour:
         return True

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_long = float(iss_data['iss_position']['longitude'])
    iss_lat = float(iss_data['iss_position']['latitude'])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= PASSWORD)
        connection.sendmail(
            msg="Subject:Look at the sky!\n\nInternational Space Station(ISS) is close to your position now.",
            from_addr= MY_EMAIL,
            to_addrs = MY_EMAIL
        )

while True:
    time.sleep(60)
    if is_night and is_iss_overhead():
        send_email()
