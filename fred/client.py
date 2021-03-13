from fred.session import FredSession
from fred.categories import Categories
from fred.releases import Releases
from fred.series import Series
from fred.sources import Sources
from fred.tags import Tags


class FederalReserveClient():

    """
    Overview:
    ----
    The `FederalReserveClient` is the main entry point to the
    different services provided by FRED. We use this object to
    initialize the other services.
    """

    def __init__(self, api_key: str) -> None:
        """Initializes the `FederalReserveClient`.

        ### Parameters
        ----
        api_key : str
            The API key assigned to you when you registered with
            FRED. For more info: https://fred.stlouisfed.org/docs/api/fred/

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
        """

        self._api_key = api_key
        self.fred_session = FredSession(client=self)

    def __repr__(self) -> str:
        """String representation of the `FederalReserveClient` object."""

        # define the string representation
        str_representation = '<FederalReserveClient (active=True, connected=True)>'

        return str_representation

    def categories(self) -> Categories:
        """Used to access the `Categories` services.

        ### Returns
        ---
        Users:
            The `Categories` services Object.
        """

        # Grab the `Categories` object.
        object = Categories(session=self.fred_session)

        return object

    def releases(self) -> Releases:
        """Used to access the `Releases` services.

        ### Returns
        ---
        Users:
            The `Releases` services Object.
        """

        # Grab the `Releases` object.
        object = Releases(session=self.fred_session)

        return object

    def series(self) -> Series:
        """Used to access the `Series` services.

        ### Returns
        ---
        Users:
            The `Series` services Object.
        """

        # Grab the `Series` object.
        object = Series(session=self.fred_session)

        return object

    def sources(self) -> Sources:
        """Used to access the `Sources` services.

        ### Returns
        ---
        Users:
            The `Sources` services Object.
        """

        # Grab the `Sources` object.
        object = Sources(session=self.fred_session)

        return object

    def tags(self) -> Tags:
        """Used to access the `Tags` services.

        ### Returns
        ---
        Users:
            The `Tags` services Object.
        """

        # Grab the `Tags` object.
        object = Tags(session=self.fred_session)

        return object
