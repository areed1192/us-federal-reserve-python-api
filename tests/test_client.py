import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient
from fred.categories import Categories
from fred.releases import Releases
from fred.sources import Sources
from fred.series import Series
from fred.tags import Tags


class FredClientTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient` Client."""

        # Read the file and get the API key.
        config = ConfigParser()
        config.read('config/config.ini')
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

    def test_creates_instance_of_releases_session(self):
        """Create an instance and make sure it's a `fred.Releases` object."""

        # Initialize the Releases Service.
        releases_services = self.fred_client.releases()
        self.assertIsInstance(releases_services, Releases)

    def test_creates_instance_of_series_session(self):
        """Create an instance and make sure it's a `fred.Series` object."""

        # Initialize the Series Service.
        series_services = self.fred_client.series()
        self.assertIsInstance(series_services, Series)

    def test_creates_instance_of_sources_session(self):
        """Create an instance and make sure it's a `fred.Sources` object."""

        # Initialize the Sources Service.
        sources_services = self.fred_client.sources()
        self.assertIsInstance(sources_services, Sources)

    def test_creates_instance_of_tags_session(self):
        """Create an instance and make sure it's a `fred.Tags` object."""

        # Initialize the Tags Service.
        tags_services = self.fred_client.tags()
        self.assertIsInstance(tags_services, Tags)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient` Client."""
        del self.fred_client


if __name__ == '__main__':
    unittest.main()
