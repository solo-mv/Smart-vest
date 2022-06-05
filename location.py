import googlemaps
from datetime import datetime
import os
from twilio.rest import Client
from twilio.rest import Client
from TTS import *
def location():
     TTS("Calculating current location")
     gmaps = googlemaps.Client(key = "key")
     location = gmaps.geolocate()
     coordinates = location['location']['lat'], location['location']['lng']
     print(coordinates)

     account_sid = 'sid'
     auth_token = 'token'
     client = Client(account_sid, auth_token)
     #
     message = client.messages.create(
          messaging_service_sid='MG53998494d257a10c06b700a37494b9d0',
          body=f"Hey, im in trouble can you provide assistance \n"
               f"Coordinates are listed in this order (latitude, longitude)\n"
               f"{coordinates}",
          to='+60173646133')
     TTS("Current location calculated, sending message")

print(message.sid)


# forms = requests.get("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCPZRtcCyMQCua0TguLHrRDGoNQ5C-4R2o")
# print(forms)
