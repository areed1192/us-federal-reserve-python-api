import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient


class SeriesTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient.Series` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient.Series` Client."""

        # Read the file and get the API key.
        config = ConfigParser()
        config.read('config/config.ini')
        api_key = config.get('main', 'api_key')

        # Initialize the Client.
        self.fred_client = FederalReserveClient(api_key=api_key)
        self.series_services = self.fred_client.series()

    def test_get_series(self):
        """Test the `get_series` method."""

        response = self.series_services.get_series(series_id='GNPCA')
        self.assertIsNotNone(response)

    def test_get_series_categories(self):
        """Test the `get_series_categories` method."""

        response = self.series_services.get_series_categories(
            series_id='EXJPUS'
        )
        self.assertIsNotNone(response)

    def test_get_series_observations(self):
        """Test the `get_series_observations` method."""

        response = self.series_services.get_series_observations(
            series_id='GNPCA'
        )
        self.assertIsNotNone(response)

    def test_get_series_release(self):
        """Test the `get_series_release` method."""

        response = self.series_services.get_series_release(series_id='IRA')
        self.assertIsNotNone(response)

    def test_get_series_updates(self):
        """Test the `get_series_updates` method."""

        response = self.series_services.get_series_updates()
        self.assertIsNotNone(response)

    def test_get_series_tags(self):
        """Test the `get_series_tags` method."""

        response = self.series_services.get_series_tags(series_id='STLFSI')
        self.assertIsNotNone(response)

    def test_get_series_vintage_dates(self):
        """Test the `get_series_vintage_dates` method."""

        response = self.series_services.get_series_vintage_dates(
            series_id='GNPCA'
        )
        self.assertIsNotNone(response)

    def test_series_search(self):
        """Test the `series_search` method."""

        response = self.series_services.series_search(
            search_text='Monetary Service Index'
        )
        self.assertIsNotNone(response)

    def test_series_tag_search(self):
        """Test the `series_tag_search` method."""

        response = self.series_services.series_tag_search(
            series_search_text='Monetary Service Index'
        )
        self.assertIsNotNone(response)

    def test_series_related_tag_search(self):
        """Test the `series_releated_tags_search` method."""

        response = self.series_services.series_releated_tags_search(
            series_search_text='Monetary Service Index',
            tag_names=['30-year', 'frb']
        )
        self.assertIsNotNone(response)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient.Series` Client."""
        del self.fred_client
        del self.series_services


if __name__ == '__main__':
    unittest.main()
