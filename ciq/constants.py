city = 'sandiego'
client_id = 'PublicAccess'
client_secret = 'uVeeMuiue4k='
api_url = "{}.cityiq.io/api/v2".format(city)
uaa_url =  "https://auth.aa.cityiq.io"
bbox = "32.703172:-117.177000,32.719981:-117.140951"


conf = {
    "uaa": uaa_url,
    "uaa_get_token": "{}/oauth/token".format(uaa_url),
    "metadata": "{}/metadata".format(api_url),
    "event":"{yourEventServiceURL}",
    "websocket": "wss://{yourWebSocketURL}",
    "developer": "{yourClientID}:{yourClientSecret}",
    "parking": "SD-IE-TRAFFIC",
    "pedestrian": "SD-IE-PEDESTRIAN",
    "traffic": "SD-IE-TRAFFIC",
    "api_url": api_url,
    "bbox": bbox,
    "client_id": client_id,
    "client_secret": client_secret,
    "city": city

    #"environment": "{yourEnvironmentPredixZoneID}",
    #"pedestrian": "{yourPedestrianPredixZoneID}",
    #"bbox": "{lat}:{long},{lat}:{long}"
}
