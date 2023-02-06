import requests
import datetime as dt
import os
from twilio.rest import Client

#----------------------------------Parameters-------------------------------#
MY_LAT = 31.2622393 # Your latitude
MY_LONG = 29.9856913 # Your longitude
apikey=os.environ.get("apikey")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

parameters={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":apikey}

now=dt.datetime.now()

if now.hour==7:
    response=requests.get("https://api.openweathermap.org/data/2.5/weather",params=parameters)
    response.raise_for_status()
    weather_data=response.json()
    condition=weather_data["weather"][0]["id"]
    if int(condition)< 700:    
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body="Bring an Umbrella with you , it's raining outside",
        from_="+1 608 975 3769",
        to="+201203846717"
        )



