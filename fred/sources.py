from typing import Dict
from typing import List
from typing import Union
from datetime import datetime
from fred.session import FredSession

# Used for type hinting
todays_date = datetime.today().date().isoformat()


class Sources():

    """
    ## Overview:
    ----
    The United States Federal Reserves many different
    sources of Economic data. The `Sources` object allows
    users to query the different sources provided by FRED
    and do complex searches when the user desires more
    specific reports.
    """

    def __init__(self, session: FredSession) -> None:
        """Initializes the `Sources` object.

        ### Parameters
        ----
        session : `FredSession`
            An initialized session of the `FredSession`.
        """

        # Set the session.
        self.fred_session: FredSession = session

        # Set the endpoint.
        self.endpoint = '/source'
        self.endpoint_collection = '/sources'
        self._todays_date = datetime.today().date().isoformat()

    def __repr__(self) -> str:
        """String representation of the `FederalReserveClient.Sources` object."""

        # define the string representation
        str_representation = '<FederalReserveClient.Sources (active=True, connected=True)>'

        return str_representation

    def get_sources(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'source_id'
    ) -> Dict:
        """Get all sources of economic data.

        ### Parameters
        ----------
        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        order_by : str (optional, Default='source_id')
            Order results by values of the specified attribute. One of the following 
            strings: ['source_id', 'name', 'realtime_start', 'realtime_end'].

        ### Returns
        ----
        Dict:
            A Collection of `Source` Resource Objects.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> sources_services = fred_client.sources()
            >>> sources_services.get_sources()
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint_collection,
            params={
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'order_by': order_by
            }
        )

        return content

    def get_source(
        self,
        source_id: int,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
    ) -> Dict:
        """Get a source of economic data.

        ### Parameters
        ----------
        source_id : int
            The ID for a source.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        ### Returns
        ----
        Dict:
            A Collection of `Source` Resource Objects.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> sources_services = fred_client.sources()
            >>> sources_services.get_source(source_id=1)
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint,
            params={
                'source_id': source_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
            }
        )

        return content

    def get_source_releases(
        self,
        source_id: int,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        order_by: str = 'release_id',
        sort_order: str = 'asc'
    ) -> Dict:
        """Get the releases for a source.

        ### Parameters
        ----------
        source_id : int
            The ID for a source.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        offset : int (optional, Default=0)
            Non-negative integer.

        order_by : str (optional, Default='release_id')
            Order results by values of the specified attribute. One of the following 
            strings: [ 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'].

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        ### Returns
        ----
        Dict:
            A Collection of `Source` Resource Objects.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> sources_services = fred_client.sources()
            >>> sources_services.get_source_releases(source_id=1)
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/releases',
            params={
                'source_id': source_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'order_by': order_by,
                'sort_order': sort_order
            }
        )

        return content
