import requests
from requests.auth import HTTPBasicAuth

def get_token():
    print("Get Token")
    url = "https://890407d7-e617-4d70-985f-01792d693387.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token"
    querystring = {"grant_type":"client_credentials"}

    response = requests.get(url, auth=HTTPBasicAuth('SanDiego','$aND!3g0'), params=querystring).json()
    token = response['access_token']
    print("Token Received")
    return token


def get_all_assets():
    print ("Get All Assets")
    url = "https://ic-metadata-service.run.aws-usw02-pr.ice.predix.io/v2/metadata/assets/search"
    querystring = {"bbox":"33.077762:-117.663817,32.559574:-116.584410","page":"0","size":"200","q":"assetType:CAMERA"}
    payload = ""

    token = get_token()

    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SDSIM-IE-TRAFFIC",
        'cache-control': "no-cache",
        'Postman-Token': "0210ae95-133f-4461-be45-1b65eda435e1"
    }

    response = requests.get(url, params=querystring, headers=headers).json()
    print(response)

def get_all_locations():
    print("Get all locations")
    url = "https://ic-metadata-service.run.aws-usw02-pr.ice.predix.io/v2/metadata/locations/search"
    querystring = {"q":"locationType:TRAFFIC_LANE","bbox":"33.077762:-117.663817,32.559574:-116.584410","page":"0","size":"50"}
    token = get_token()
    headers = {
        'Authorization': "Bearer {}".format(token),
        'Predix-Zone-Id': "SDSIM-IE-TRAFFIC",
        'cache-control': "no-cache",
        'Postman-Token': "0210ae95-133f-4461-be45-1b65eda435e1"
    }
    response = requests.get(url, params=querystring, headers=headers).json()
    print(response)

#get_all_locations()
