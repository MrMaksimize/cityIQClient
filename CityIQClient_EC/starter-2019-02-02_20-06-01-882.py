import requests
from requests.auth import HTTPBasicAuth
from cityCredentials import client
from cityCredentials import secret
from cityCredentials import parking
from cityCredentials import environment
from cityCredentials import pedestrian
from cityCredentials import traffic
from cityCredentials import video
from cityCredentials import images
from cityCredentials import bbox
import datetime
from datetime import timedelta

#using your clientID and Client secret (stored on your machine as variables) this function will return a CityIQ token
def get_token():
    print("Get Token")
    url = 'https://624eff02-dbb1-4c6c-90bc-fa85a29e5fa8.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'
    querystring = {"grant_type":"client_credentials"}

    response = requests.get(url, auth=HTTPBasicAuth(client,secret), params=querystring).json()
    token = response['access_token']
    print("Token Received")
    return token

# returns a list of all requested assets based within the specified predix zone and bbox
def get_assets():
    assetType = "assetType:CAMERA"
    url = "https://ic-metadata-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/metadata/assets/search"
    querystring = {bbox:"","page":"0","size":"200","q":assetType}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-TRAFFIC",
        'cache-control': "no-cache",
        'Postman-Token': "81281f86-66f2-461d-a33b-6e5794ac3b51"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#give it an CityIQ node ID and it will return the asset details.
def get_asset_details():
    asset = "ae7f70bd-2585-4c60-9252-5dfd472b9dda"
    url = "https://ic-metadata-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/metadata/assets/" + asset
    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-TRAFFIC",
        'cache-control': "no-cache",
        'Postman-Token': "e4c6322e-2360-4b7c-8420-037c5e68313b"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)


#get traffic events from a specified asset starting at a point in the past and ending now
def get_traffic_event_by_asset(asset, start):
    asset = "ae7f70bd-2585-4c60-9252-5dfd472b9dda"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc = ts-start
    CityIQ_Starttime_TS = int(CityIQ_TS_Calc * 1000)
    #CityIQ_Starttime_TS = int((ts-start)*1000)
    querystring = {"eventType":"TFEVT","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-TRAFFIC",
        'cache-control': "no-cache",
        'Postman-Token': "8f48306c-1b97-4c64-8654-84dc8c4d00a0"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)

asset = "ae7f70bd-2585-4c60-9252-5dfd472b9dda"
lookback_minutes = 600
ts = datetime.datetime.now().timestamp()
CityIQ_Current_TS = int(ts*1000)
CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
CityIQ_Starttime_TS =  CityIQ_TS_Calc_TS
print(CityIQ_Current_TS)
print(CityIQ_Starttime_TS)

#get_traffic_event_by_asset(asset, start)
