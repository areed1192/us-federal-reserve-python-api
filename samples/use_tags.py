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

# Initialize the `Tags` Service.
tags_services = fred_client.tags()

# Grab all the Tags.
pprint(tags_services.get_tags())

# Grab all the Related Tags.
pprint(
    tags_services.get_related_tags(
        tag_names=['monetary aggregates', 'weekly']
    )
)

# Grab all the Tags for a series.
pprint(
    tags_services.get_tags_series(
        tag_names=['slovenia', 'food', 'oecd']
    )
)
