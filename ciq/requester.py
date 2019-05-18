import requests
from requests.auth import HTTPBasicAuth
import logging
from ciq.constants import conf

from urllib.parse import urlencode, urlparse, urljoin, urlunparse, parse_qs



class CIQHttpClient(object):
    """
    General purpose HTTP Client for interacting with the CityIQ API
    """
    def __init__(self, username, password):
        self.last_response = None
        self.access_token = None
        self.access_token = self.get_token(username, password)

    def get_token(self, username, password):
        # TODO use the request method I'm already writing
        print("Get Token")
        url = conf['uaa_get_token']
        querystring = {"grant_type":"client_credentials"}
        response = requests.get(url, auth = HTTPBasicAuth(
            conf['client_id'],conf['client_secret']), params=querystring).json()
        token = response['access_token']
        print("Token Received")
        return token



    def make_request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None):
        """
        Make an HTTP Request with parameters provided.
        :param str method: The HTTP method to use
        :param str url: The URL to request
        :param dict params: Query parameters to append to the URL
        :param dict data: Parameters to go in the body of the HTTP request
        :param dict headers: HTTP Headers to send with the request
        :param tuple auth: Basic Auth arguments
        :param float timeout: Socket/Read timeout for the request
        See the requests documentation for explanation of all these parameters
        :return: An http response
        """

        kwargs = {
            'method': method.upper(),
            'url': url,
            'params': params,
            'data': data,
            'headers': headers,
            'auth': auth
        }

        if params:
            _logger.info('{method} Request: {url}?{query}'.format(query=urlencode(params), **kwargs))
            _logger.info('PARAMS: {params}'.format(**kwargs))
        else:
            _logger.info('{method} Request: {url}'.format(**kwargs))
        if data:
            _logger.info('PAYLOAD: {data}'.format(**kwargs))

        self.last_response = None

        if self.access_token == None:
            self.access_token = self.get_token()

        # Inject auth and cache controls into whatever other headers
        added_headers = {
            'Authorization': "Bearer {}".format(self.access_token),
            'cache-control':  "no-cache"
        }
        kwargs['headers'] = {**kwargs['headers'], **added_headers}

        response = requests.request(**kwargs)
        self.last_response = response
        return response

    def get_locations(self, location_type=None, bbox=None):
        print("Get all locations")
        url = "https://ic-metadata-service.run.aws-usw02-pr.ice.predix.io/v2/metadata/locations/search"
        querystring = {
                "q":"locationType:TRAFFIC_LANE",
                "bbox":"33.077762:-117.663817,32.559574:-116.584410",
                "page":"0",
                "size":"50"
        }
        headers = {
            'Predix-Zone-Id': "SDSIM-IE-TRAFFIC",
        }
        return self.make_request("GET", url=url, params=querystring, headers=headers).json()

    def getLocation(self, uid):










        #_logger.info('{method} Response: {status} {text}'.format(method=method, status=response.status_code, text=response.text))

        #self.last_response = Response(int(response.status_code), response.text)

        return self.last_response
