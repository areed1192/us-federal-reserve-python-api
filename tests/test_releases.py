import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient


class ReleasesTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient.Releases` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient.Releases` Client."""

        # Read the file and get the API key.
        config = ConfigParser()
        config.read('config/config.ini')
        api_key = config.get('main', 'api_key')

        # Initialize the Client.
        self.fred_client = FederalReserveClient(api_key=api_key)
        self.releases_services = self.fred_client.releases()

    def test_get_releases(self):
        """Test the `get_releases` method."""

        response = self.releases_services.get_releases()
        self.assertIsNotNone(response)

    def test_get_releases_dates(self):
        """Test the `get_releases_dates` method."""

        response = self.releases_services.get_releases_dates()
        self.assertIsNotNone(response)

    def test_get_release_by_id(self):
        """Test the `get_release_by_id` method."""

        response = self.releases_services.get_release_by_id(release_id='53')
        self.assertIsNotNone(response)

    def test_get_release_dates(self):
        """Test the `get_release_dates` method."""

        response = self.releases_services.get_release_dates(release_id='53')
        self.assertIsNotNone(response)

    def test_get_release_series(self):
        """Test the `get_release_series` method."""

        response = self.releases_services.get_release_series(release_id='53')
        self.assertIsNotNone(response)

    def test_get_release_sources(self):
        """Test the `get_release_sources` method."""

        response = self.releases_services.get_release_sources(release_id='51')
        self.assertIsNotNone(response)

    def test_get_release_related_tags(self):
        """Test the `get_release_related_tags` method."""

        response = self.releases_services.get_release_related_tags(
            release_id='86'
        )
        self.assertIsNotNone(response)

    def test_get_release_tags(self):
        """Test the `get_release_tags` method."""

        response = self.releases_services.get_release_tags(release_id='86')
        self.assertIsNotNone(response)

    def test_get_release_tables(self):
        """Test the `get_release_tables` method."""

        response = self.releases_services.get_release_tables(release_id='53')
        self.assertIsNotNone(response)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient.Releases` Client."""
        del self.fred_client
        del self.releases_services


if __name__ == '__main__':
    unittest.main()
