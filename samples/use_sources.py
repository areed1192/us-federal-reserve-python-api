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

# Initialize the `Sources` Service.
sources_services = fred_client.sources()

# Grab all the data sources.
pprint(sources_services.get_sources())

# Grab a specific source.
pprint(sources_services.get_source(source_id=1))

# Grab the releases for a specific source.
pprint(sources_services.get_source_releases(source_id=1))
