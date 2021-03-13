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

# Initialize the Releases Service.
releases_service = fred_client.releases()

# Grab some releases.
pprint(releases_service.get_releases())

# Grab the Release dates.
pprint(releases_service.get_releases_dates())

# Grab a release by it's ID.
pprint(releases_service.get_release_by_id(release_id='53'))

# Grab the dates for a particular release.
pprint(releases_service.get_release_dates(release_id='53'))

# Get the series for a particular release.
pprint(releases_service.get_release_series(release_id='53'))

# Get the sources for a particular release.
pprint(releases_service.get_release_sources(release_id='51'))

# Get the tags for a particular release.
pprint(releases_service.get_release_tags(release_id='86'))

# Get the releated tags for a particular release.
pprint(releases_service.get_release_related_tags(release_id='86'))

# Get the tables for a particular release.
pprint(releases_service.get_release_tables(release_id='53'))
