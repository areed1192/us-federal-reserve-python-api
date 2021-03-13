import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient


class SourcesTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient.Sources` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient.Sources` Client."""

        # Read the file and get the API key.
        config = ConfigParser()
        config.read('config/config.ini')
        api_key = config.get('main', 'api_key')

        # Initialize the Client.
        self.fred_client = FederalReserveClient(api_key=api_key)
        self.sources_services = self.fred_client.sources()

    def test_get_sources(self):
        """Test the `get_sources` method."""

        response = self.sources_services.get_sources()
        self.assertIsNotNone(response)

    def test_get_source(self):
        """Test the `get_source` method."""

        response = self.sources_services.get_source(source_id=1)
        self.assertIsNotNone(response)

    def test_get_source_releases(self):
        """Test the `get_sources` method."""

        response = self.sources_services.get_source_releases(source_id=1)
        self.assertIsNotNone(response)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient.Sources` Client."""
        del self.fred_client
        del self.sources_services


if __name__ == '__main__':
    unittest.main()
