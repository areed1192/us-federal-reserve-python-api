from pprint import pprint
from configparser import ConfigParser
from fred.client import FederalReserveClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
api_key = config.get('main', 'api_key')

# Initialize the Client.
fred_client = FederalReserveClient(api_key=api_key)

# Initialize the Categories Service.
categories_service = fred_client.categories()

# Grab a category by it's ID.
pprint(categories_service.get_category(category_id='125'))

# Grab a categories children.
pprint(categories_service.get_category(category_id='13'))

# Grab related categories.
pprint(categories_service.get_related_category(category_id='32073'))

# Grab a category's series.
pprint(categories_service.get_category_series(category_id='125'))

# Grab a category's tags.
pprint(categories_service.get_category_tags(category_id='125'))

# Grab a category's related tags.
pprint(categories_service.get_related_category_tags(category_id='125'))