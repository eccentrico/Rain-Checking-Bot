import requests
from twilio.rest import Client
account_sid = 'ACbf83427fb8ecf4bb58ad1f26005f077c'
auth_token = "f09bc07563fa5ca815cad2cdaa575008"
parameters={"lat":"46.947975",
           "lon":"7.447447",
           "appid":"8c03dd38505739fd112954b94f905868",
            "exclude": "current,minutely,daily"}


response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
response.raise_for_status()
data=response.json()
list_to_slice=data["hourly"]
sliced_list=list_to_slice[0:13]
will_rain=False
for id in sliced_list:
    condition_code=int(id["weather"][0]["id"])
    if condition_code <700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It will rain, bring an umbrella with yourself ",
        from_="+14092634731",
        to="+91 78897 69991"
    )
    print(message.status)
