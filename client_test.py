import requests
from requests.auth import HTTPBasicAuth
from ciq.requester import CIQHttpClient


ciq = CIQHttpClient('PublicAccess', 'uVeeMuiue4k=')
print(ciq.access_token)

#locs = ciq.get_locations(location_type=None, bbox=None)
#print(locs.keys())
#print(locs['content'][0])

location = ciq.getLocations[0]

location.update
