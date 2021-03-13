import json
import requests
import logging

from typing import Dict


class FredSession():

    """Serves as the Session for the Current FRED
    API."""

    def __init__(self, client: object) -> None:
        """Initializes the `FredSession` client.

        ### Overview:
        ----
        The `FredSession` object handles all the requests made
        for the different endpoints on the FRED API.

        ### Arguments:
        ----
        client (str): The `fred.FederalReserveClient` Python Client.

        ### Usage:
        ----
            >>> fred_session = FredSession()
        """

        from fred.client import FederalReserveClient

        # We can also add custom formatting to our log messages.
        log_format = '%(asctime)-15s|%(filename)s|%(message)s'

        self.client: FederalReserveClient = client
        self.resource = 'https://api.stlouisfed.org/fred'

        logging.basicConfig(
            filename="logs/log_file_custom.log",
            level=logging.INFO,
            encoding="utf-8",
            format=log_format
        )

    def build_url(self, endpoint: str) -> str:
        """Builds the full url for the endpoint.

        ### Parameters
        ----
        endpoint : str
            The endpoint being requested.

        ### Returns
        ----
        str:
            The full URL with the endpoint needed.
        """

        url = self.resource + endpoint

        return url

    def make_request(
            self,
            method: str,
            endpoint: str,
            mode: str = None,
            params: dict = None,
            data: dict = None,
            json_payload: dict = None,
            order_details: bool = False
        ) -> Dict:
        """Handles all the requests in the library.

        ### Overview:
        ---
        A central function used to handle all the requests made in the library,
        this function handles building the URL, defining Content-Type, passing
        through payloads, and handling any errors that may arise during the request.

        ### Arguments:
        ----
        method: The Request method, can be one of the
            following: ['get','post','put','delete','patch']

        endpoint: The API URL endpoint, example is 'quotes'

        mode: The content-type mode, can be one of the
            following: ['form','json']

        params: The URL params for the request.

        data: A data payload for a request.

        json: A json data payload for a request

        ### Returns:
        ----
        A Dictionary object containing the JSON values.
        """

        # Build the URL.
        url = self.build_url(endpoint=endpoint)

        logging.info(
            "URL: {url}".format(url=url)
        )

        # Define a new session.
        request_session = requests.Session()
        request_session.verify = True

        # Define a new request.
        request_request = requests.Request(
            method=method.upper(),
            url=url,
            params=params,
            data=data,
            json=json_payload
        ).prepare()

        # Send the request.
        response: requests.Response = request_session.send(
            request=request_request
        )

        # Close the session.
        request_session.close()

        # If it's okay and no details.
        if response.ok and len(response.content) > 0:
            return response.json()
        elif len(response.content) > 0 and response.ok:
            return {
                'message': 'response successful',
                'status_code': response.status_code
            }
        elif not response.ok:

            # Define the error dict.
            error_dict = {
                'error_code': response.status_code,
                'response_url': response.url,
                'response_body': json.loads(response.content.decode('ascii')),
                'response_request': dict(response.request.headers),
                'response_method': response.request.method,
            }

            # Log the error.
            logging.error(
                msg=json.dumps(obj=error_dict, indent=4)
            )

            raise requests.HTTPError()
