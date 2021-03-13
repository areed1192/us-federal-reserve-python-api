
from typing import List
from typing import Dict
from typing import Union

from fred.session import FredSession


class FederalReserveClient():


    def __init__(self, api_key: str) -> None:
        """Initializes the `FederalReserveClient`.

        ### Parameters
        ----
        api_key : str
            The API key assigned to you when you registered with
            FRED. For more info: https://fred.stlouisfed.org/docs/api/fred/
        """

        self._api_key = api_key
        self.fred_session = FredSession(client=self)


    def __repr__(self):
        pass
