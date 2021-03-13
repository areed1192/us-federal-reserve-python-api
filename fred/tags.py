from typing import Dict
from typing import List
from typing import Union
from datetime import datetime
from fred.session import FredSession

# Used for type hinting
todays_date = datetime.today().date().isoformat()


class Tags():

    """
    ## Overview:
    ----
    FRED tags are attributes assigned to series. Related FRED tags 
    are the tags assigned to series that match all tags in the tag_names
    parameter and no tags in the exclude_tag_names parameter. This service
    will help you search for tags so that you can use them in other more
    complex queries.
    """

    def __init__(self, session: FredSession) -> None:
        """Initializes the `Tags` object.

        ### Parameters
        ----
        session : `FredSession`
            An initialized session of the `FredSession`.
        """

        # Set the session.
        self.fred_session: FredSession = session

        # Set the endpoint.
        self.endpoint = '/tag'
        self.endpoint_collection = '/tags'

    def __repr__(self) -> str:
        """String representation of the `FederalReserveClient.Tags` object."""

        # define the string representation
        str_representation = '<FederalReserveClient.Tags (active=True, connected=True)>'

        return str_representation

    def get_tags(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'series_count',
        tag_names: List[str] = None,
        tag_group_id: str = None,
        search_text: str = None
    ) -> Dict:
        """Get FRED tags. Optionally, filter results by tag name, tag group, or search. 
        FRED tags are attributes assigned to series.

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

        order_by : str (optional, Default='series_count')
            Order results by values of the specified attribute. One of the following 
            strings: [ 'series_count', 'popularity', 'created', 'name', 'group_id'].

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match all of.

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen',
            'geo', 'geot', 'rls', 'seas', 'src', 'cc'].

        search_text : str (optional, Default=None)
            The words to find matching tags with.

        ### Returns
        ----
        Dict:
            A Collection of `Tag` Resource Objects.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> tag_services = fred_client.tags()
            >>> tag_services.get_tags()
        """

        if tag_names:
            tag_names = ';'.join(tag_names)

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
                'order_by': order_by,
                'tag_names': tag_names,
                'tag_group_id': tag_group_id,
                'search_text': search_text
            }
        )

        return content

    def get_related_tags(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'series_count',
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None,
        tag_group_id: str = None,
        search_text: str = None
    ) -> Dict:
        """Get the related FRED tags for one or more FRED tags. Optionally,
        filter results by tag group or search.

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

        order_by : str (optional, Default='series_count')
            Order results by values of the specified attribute. One of the following 
            strings: ['series_count', 'popularity', 'created', 'name', 'group_id'].

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match all of.

        exclude_tag_names : List[str] (optional, Default=None)
            A list of tag names that series match None of.

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen',
            'geo', 'geot', 'rls', 'seas', 'src'].

        search_text : str (optional, Default=None)
            The words to find matching tags with.

        ### Returns
        ----
        Dict:
            A Collection of `Tag` Resource Objects.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> tag_services = fred_client.tags()
            >>> tag_services.get_related_tags(tag_names=['monetary aggregates', 'weekly'])
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint='/related_tags',
            params={
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'order_by': order_by,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names,
                'tag_group_id': tag_group_id,
                'search_text': search_text
            }
        )

        return content

    def get_tags_series(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'series_id',
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None,
        tag_group_id: str = None
    ) -> Dict:
        """Get the related FRED tags for one or more FRED tags. Optionally,
        filter results by tag group or search.

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

        order_by : str (optional, Default='series_id')
            Order results by values of the specified attribute. One of the following 
            strings: ['series_id', 'title', 'units', 'frequency', 'seasonal_adjustment',
            'realtime_start', 'realtime_end', 'last_updated', 'observation_start',
            'observation_end', 'popularity', 'group_popularity'].

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match all of.

        exclude_tag_names : List[str] (optional, Default=None)
            A list of tag names that series match None of.

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen',
            'geo', 'geot', 'rls', 'seas', 'src'].

        ### Returns
        ----
        Dict:
            A Collection of `Tag` Resource Objects.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> tag_services = fred_client.tags()
            >>> tag_services.get_tags_series(tag_names=['slovenia', 'food', 'oec'])
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint='/tags/series',
            params={
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'order_by': order_by,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names,
                'tag_group_id': tag_group_id
            }
        )

        return content
