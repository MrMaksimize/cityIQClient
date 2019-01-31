import requests
from requests import Request, Session, hooks
from requests.auth import HTTPBasicAuth

class CIQHttpClient(object):
    """
    General purpose HTTP Client for interacting with the CityIQ API
    """
    def __init__(self, username, password):
        self.last_request = None
        self.last_response = None
        self.access_token = None
        self.access_token = self.get_token(username, password)


    def get_token(self, username, password):
        # TODO use the request method I'm already writing
        print("Get Token")
        url = "https://890407d7-e617-4d70-985f-01792d693387.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token"
        querystring = {"grant_type":"client_credentials"}
        response = requests.get(url, auth=HTTPBasicAuth('SanDiego','$aND!3g0'), params=querystring).json()
        token = response['access_token']
        print("Token Received")
        return token



    def request(self, method, url, params=None, data=None, headers=None, auth=None, timeout=None):
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

        if access_token == None:
            self.access_token = self.get_token()

        request = Request(**kwargs)
        self.last_request = request






        #_logger.info('{method} Response: {status} {text}'.format(method=method, status=response.status_code, text=response.text))

        #self.last_response = Response(int(response.status_code), response.text)

        return self.last_response
