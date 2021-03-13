import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient


class TagsTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient.Tags` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient.Tag` Client."""

        # Read the file and get the API key.
        config = ConfigParser()
        config.read('config/config.ini')
        api_key = config.get('main', 'api_key')

        # Initialize the Client.
        self.fred_client = FederalReserveClient(api_key=api_key)
        self.tags_services = self.fred_client.tags()

    def test_get_tags(self):
        """Test the `get_tags` method."""

        response = self.tags_services.get_tags()
        self.assertIsNotNone(response)

    def test_get_related_tags(self):
        """Test the `get_related_tags` method."""

        response = self.tags_services.get_related_tags(
            tag_names=['monetary aggregates', 'weekly']
        )
        self.assertIsNotNone(response)

    def test_get_series_tags(self):
        """Test the `get_series_tags` method."""

        response = self.tags_services.get_tags_series(
            tag_names=['slovenia', 'food', 'oecd']
        )
        self.assertIsNotNone(response)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient.Tags` Client."""
        del self.fred_client
        del self.tags_services


if __name__ == '__main__':
    unittest.main()
