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

# returns a list of all requested assets based within the specified assetType, predix zone and bboxself.
#assetTypes can be 'CAMERA', 'ENV_SENSOR', 'NODE'(parent asset), 'OTHERS' (list of non-standard devices)
#predix zones are 'SD-IE-PARKING', 'SD-IE-ENVIRONMENTAL','SD-IE-PEDESTRIAN', 'SD-IE-TRAFFIC'
def get_assets():
    assetType = "assetType:CAMERA"
    url = "https://ic-metadata-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/metadata/assets/search"
    querystring = {bbox:"","page":"0","size":"200","q":assetType}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-PARKING",
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
#you need to give it CityIQ assetUID (a string) and lookback_minutes, the number of minutes
#before the current time a the starting point for the search as a (int).
#DONT THINK THIS IS WORKING, IT ISNT RETURNING DATA
def get_traffic_event_by_asset(asset, lookback_minutes):
    asset = "92e6fb6e-f352-49ea-86f2-16d626f3d271"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
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

asset = "b2d79d52-2310-4ff2-b725-cd3c2a817b69"
lookback_minutes = 600


#DONT THINK THIS IS WORKING, IT ISNT RETURNING DATA
def get_traffic_event_by_bbox(lookback_minutes):
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets"+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"TFEVT","bbox":"","locationType":"TRAFFIC_LANE","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

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

lookback_minutes = 600

#get current temperature by asset
def get_temp():
    asset = "0e6199d6-33b1-45d0-aa09-3dd51c04a77c"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)

    querystring = {"eventType":"TEMPERATURE","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-ENVIRONMENTAL",
        'cache-control': "no-cache",
        'Postman-Token': "dbd024e1-21a0-48d0-bf0d-3305d7d2396d"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)


#get current pressure by asset
def get_pressure():
    asset = "0e6199d6-33b1-45d0-aa09-3dd51c04a77c"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PRESSURE","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-ENVIRONMENTAL",
        'cache-control': "no-cache",
        'Postman-Token': "79a9e5c2-c1dc-4dc3-bbe4-34c751fa389e"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#get current orientation by asset
def get_orientation():
    asset = "0e6199d6-33b1-45d0-aa09-3dd51c04a77c"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"ORIENTATION","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-ENVIRONMENTAL",
        'cache-control': "no-cache",
        'Postman-Token': "79a9e5c2-c1dc-4dc3-bbe4-34c751fa389e"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#get current humidity by asset
def get_humidity():
    asset = "0e6199d6-33b1-45d0-aa09-3dd51c04a77c"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"HUMIDITY","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SD-IE-ENVIRONMENTAL",
        'cache-control': "no-cache",
        'Postman-Token': "79a9e5c2-c1dc-4dc3-bbe4-34c751fa389e"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#get pedestrian count by asset
def get_ped_by_asset():
    asset = "0297e736-88e8-4a4a-8da0-be7f2dae52de"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PEDEVT","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
    'Predix-Zone-Id': "SD-IE-PEDESTRIAN",
    'cache-control': "no-cache",
    'Postman-Token': "944b1e16-6cfe-4970-ba30-5048e6b291e7"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)


#get pedestrian count by bbox
def get_ped_by_bbox():
    bbox = '32.7225326:-117.1674644,32.7176702:-117.1625865'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/locations/events"
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PEDEVT","bbox":bbox,"locationType":"WALKWAY","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
    'Predix-Zone-Id': "SD-IE-PEDESTRIAN",
    'cache-control': "no-cache",
    'Postman-Token': "def220c5-80b6-4087-b81c-fee544d3077d"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#get parking IN count by asset
def get_PKIN_by_asset():
    asset = "027c652c-f764-422d-88d2-d6796b6eb17e"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PKIN","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
    'Predix-Zone-Id': "SD-IE-PARKING",
    'cache-control': "no-cache",
    'Postman-Token': "944b1e16-6cfe-4970-ba30-5048e6b291e7"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#get parking IN count by bbox
def get_PKIN_by_bbox():
    bbox = '32.7225326:-117.1674644,32.7176702:-117.1625865'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/locations/events"
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PKIN","bbox":bbox,"locationType":"PARKING_ZONE","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
    'Predix-Zone-Id': "SD-IE-PARKING",
    'cache-control': "no-cache",
    'Postman-Token': "def220c5-80b6-4087-b81c-fee544d3077d"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)


#get parking OUT count by asset
def get_PKOUT_by_asset():
    asset = "027c652c-f764-422d-88d2-d6796b6eb17e"
    url_string = '/events'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/assets/"+asset+url_string
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PKOUT","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
    'Predix-Zone-Id': "SD-IE-PARKING",
    'cache-control': "no-cache",
    'Postman-Token': "944b1e16-6cfe-4970-ba30-5048e6b291e7"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

#get parking OUT count by bbox
def get_PKOUT_by_bbox():
    bbox = '32.7225326:-117.1674644,32.7176702:-117.1625865'
    url = "https://ic-event-service-sandiego.run.aws-usw02-pr.ice.predix.io/v2/locations/events"
    ts = datetime.datetime.now().timestamp()
    CityIQ_Current_TS = int(ts*1000)
    CityIQ_TS_Calc_TS =  datetime.datetime.now() - timedelta(minutes=lookback_minutes)
    CityIQ_Starttime_TS =  int((ts-(lookback_minutes*60))*1000)
    querystring = {"eventType":"PKOUT","bbox":bbox,"locationType":"PARKING_ZONE","startTime":CityIQ_Starttime_TS,"endTime":CityIQ_Current_TS,"pageSize":"100"}

    payload = ""
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
    'Predix-Zone-Id': "SD-IE-PARKING",
    'cache-control': "no-cache",
    'Postman-Token': "def220c5-80b6-4087-b81c-fee544d3077d"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)

get_PKOUT_by_bbox()
