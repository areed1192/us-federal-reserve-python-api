import unittest

from unittest import TestCase
from configparser import ConfigParser
from fred.client import FederalReserveClient


class CategoriesTest(TestCase):

    """Will perform a unit test for the `FederalReserveClient.Categories` session."""

    def setUp(self) -> None:
        """Set up the `FederalReserveClient.Categories` Client."""

        # Read the file and get the API key.
        config = ConfigParser()
        config.read('config/config.ini')
        api_key = config.get('main', 'api_key')

        # Initialize the Client.
        self.fred_client = FederalReserveClient(api_key=api_key)
        self.categories_services = self.fred_client.categories()

    def test_get_category(self):
        """Test the `get_category` method."""

        response = self.categories_services.get_category(category_id='125')
        self.assertIsNotNone(response)

    def test_get_category_children(self):
        """Test the `get_category_children` method."""

        response = self.categories_services.get_category_children(
            category_id='13'
        )
        self.assertIsNotNone(response)

    def test_get_related_category(self):
        """Test the `get_related_category` method."""

        response = self.categories_services.get_related_category(
            category_id='32073'
        )
        self.assertIsNotNone(response)

    def test_get_category_series(self):
        """Test the `get_category_series` method."""

        response = self.categories_services.get_category_series(
            category_id='125'
        )
        self.assertIsNotNone(response)

    def test_get_category_tags(self):
        """Test the `get_category_tags` method."""

        response = self.categories_services.get_category_tags(
            category_id='125'
        )
        self.assertIsNotNone(response)

    def test_get_related_category_tags(self):
        """Test the `get_related_category_tags` method."""

        response = self.categories_services.get_related_category_tags(
            category_id='125'
        )
        self.assertIsNotNone(response)

    def tearDown(self) -> None:
        """Teardown the `FederalReserveClient.Categories` Client."""
        del self.fred_client
        del self.categories_services


if __name__ == '__main__':
    unittest.main()
