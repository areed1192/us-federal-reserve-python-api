import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient
from fred.categories import Categories


class FredClientTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient` Client."""

        # Initialize the Parser.
        config = ConfigParser()

        # Read the file.
        config.read('config/config.ini')

        # Get the specified credentials.
        api_key = config.get('main', 'api_key')

        # Initialize the Client.
        self.fred_client = FederalReserveClient(api_key=api_key)

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `FederalReserveClient` object."""

        self.assertIsInstance(self.fred_client, FederalReserveClient)

    def test_creates_instance_of_categories_session(self):
        """Create an instance and make sure it's a `fred.Categories` object."""

        # Initialize the Categories Service.
        categories_service = self.fred_client.categories()

        self.assertIsInstance(categories_service, Categories)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient` Client."""
        del self.fred_client


if __name__ == '__main__':
    unittest.main()
