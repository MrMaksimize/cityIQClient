import requests
from requests.auth import HTTPBasicAuth
import logging
from urllib.parse import urlencode, urlparse, urljoin, urlunparse, parse_qs
import constants
import CIQHttpClient


class CIQLocation(object):
    """
    General purpose HTTP Client for interacting with the CityIQ API
    """
    def __init__(self, requester, uid):
        self.uid = uid
        self.requester = requester

    def update(self):
        url = "{}/locations/{}".format(METADATA_URL, self.uid)
        headers = {
            'Predix-Zone-Id': "SDSIM-IE-TRAFFIC"
        }

        resp = r




