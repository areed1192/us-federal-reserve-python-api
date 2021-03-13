from fred.client import FederalReserveClient
from pprint import pprint
from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
api_key = config.get('main', 'api_key')

# Initialize the Client.
fred_client = FederalReserveClient(api_key=api_key)

# Initialize the `Series` Service.
series_service = fred_client.series()

# Grab a specific series.
pprint(series_service.get_series(series_id='GNPCA'))

# Grab the categories for a specific series.
pprint(series_service.get_series_categories(series_id='EXJPUS'))

# Grab the observatiosn for a specific series.
pprint(series_service.get_series_observations(series_id='GNPCA'))

# Grab the releases for a specific series.
pprint(series_service.get_series_releases(series_id='IRA'))

# Search for series that contain the phrase 'Monetary Service Index'.
pprint(series_service.series_search(search_text='Monetary Service Index'))

# Grab the FRED Tags for a series search.
pprint(
    series_service.series_tag_search(
        series_search_text='Monetary Service Index'
    )
)

# Grab the Related FRED Tags for a searies search.
pprint(
    series_service.series_tag_search(
        series_search_text='Mortgage Rates',
        tag_names=['30-year', 'frb']
    )
)

# Grab the Tags for a specific Series.
pprint(series_service.get_series_tags(series_id='STLFSI'))

# Grab the Series Updates.
pprint(series_service.get_series_updates())

# Grab the Vintage Dates for a specific series.
pprint(series_service.get_series_vintage_dates(series_id='GNPCA'))
