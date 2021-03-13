from typing import Dict
from typing import List
from typing import Union
from datetime import datetime
from fred.session import FredSession

# Used for type hinting
todays_date = datetime.today().date().isoformat()


class Categories():

    """
    ## Overview:
    ----
    The Federal Reserve use high-level categories to organize their
    economic data. The `Categories` service allows users to grab category
    names and metadata that can be used in other requests. Additionally,
    you'll be able to identify relationships between different categories.
    """

    def __init__(self, session: FredSession) -> None:
        """Initializes the `Categories` object.

        ### Parameters
        ----
        session : `FredSession`
            An initialized session of the `FredSession`.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
        """

        # Set the session.
        self.fred_session: FredSession = session

        # Set the endpoint.
        self.endpoint = '/category'

    def __repr__(self) -> str:
        """String representation of the `FederalReserveClient.Categories` object."""

        # define the string representation
        str_representation = '<FederalReserveClient.Categories (active=True, connected=True)>'

        return str_representation

    def get_category(self, category_id: str) -> Dict:
        """Gets a category by it's Category ID.

        ### Parameters
        ----
        category_id : str
            The category ID you want to query.

        ### Returns
        ----
        Dict:
            A `Category` Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
            >>> categories_service.get_category(category_id='125')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint,
            params={
                'category_id': category_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json'
            }
        )

        return content

    def get_category_children(self, category_id: str) -> Dict:
        """Gets the children of the category being queried.

        ### Parameters
        ----
        category_id : str
            The category ID you want to query.

        ### Returns
        ----
        Dict:
            A `Category` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
            >>> categories_service.get_category(category_id='13')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/children',
            params={
                'category_id': category_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json'
            }
        )

        return content

    def get_related_category(self, category_id: str) -> Dict:
        """Get the related categories for a category.

        ### Overview
        -----
        A related category is a one-way relation between 2
        categories that is not part of a parent-child category
        hierarchy. Most categories do not have related categories.

        ### Parameters
        ----
        category_id : str
            The category ID you want to query.

        ### Returns
        ----
        Dict:
            A `Category` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
            >>> categories_service.get_related_category(category_id='32073')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/related',
            params={
                'category_id': category_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json'
            }
        )

        return content

    def get_category_series(
        self,
        category_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        order_by: str = 'series_id',
        sort_order: str = 'asc',
        filter_variable: str = None,
        filter_value: str = None,
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None
    ) -> Dict:
        """Get the series in a category.

        ### Parameters
        ----
        category_id : str
            The category ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        order_by : str (optional, Default='series_id')
            One of the following strings: ['series_id', 'title', 'units', 'frequency',
            'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated',
            'observation_start', 'observation_end', 'popularity', 'group_popularity'].

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        filter_variable : str (optional, Default=None)
            The attribute to filter results by. On of the following strings:
            ['frequency', 'units', 'seasonal_adjustment'].

        filter_value : str (optional, Default=None)
            The value of the filter_variable attribute to filter results by.

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match ALL of.Example value: ['income','bea'].
            See the related request: https://fred.stlouisfed.org/docs/api/fred/tags.html.

        exclude_tag_names : List[str] (optional, Default=None)
            A list of tag names that series match NONE of. Example value: ['income','bea'].
            See the related request: https://fred.stlouisfed.org/docs/api/fred/tags.html.

        ### Returns
        ----
        Dict:
            A `Category` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
            >>> categories_service.get_category_series(category_id='125')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/series',
            params={
                'category_id': category_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'order_by': order_by,
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'sort_order': sort_order,
                'filter_variable': filter_variable,
                'filter_value': filter_value,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names
            }
        )

        return content

    def get_category_tags(
        self,
        category_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        order_by: str = 'series_count',
        sort_order: str = 'asc',
        tag_names: List[str] = None,
        tag_group_id: str = None,
        search_text: str = None
    ) -> Dict:
        """Get the FRED tags for a category.

        ### Overview
        ----
        Optionally, filter results by tag name, tag group, or search.
        Series are assigned tags and categories. Indirectly through 
        series, it is possible to get the tags for a category. No tags
        exist for a category that does not have series. See the related
        request fred/category/related_tags.

        ### Parameters
        ----
        category_id : str
            The category ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        order_by : str (optional, Default='series_count')
            Order results by values of the specified attribute. One of the
            following strings: ['series_count', 'popularity', 'created',
            'name', 'group_id'].

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match ALL of.Example value: ['income','bea'].
            See the related request: https://fred.stlouisfed.org/docs/api/fred/tags.html.

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen',
            'geo', 'geot', 'rls', 'seas', 'src'].

        search_text : str (optional, Default=None)
            The words to find matching tags with.

        ### Returns
        ----
        Dict:
            A `Category` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
            >>> categories_service.get_category_tags(category_id='125')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/tags',
            params={
                'category_id': category_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'order_by': order_by,
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'sort_order': sort_order,
                'tag_names': tag_names,
                'tag_group_id': tag_group_id,
                'search_text': search_text
            }
        )

        return content

    def get_related_category_tags(
        self,
        category_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        order_by: str = 'series_count',
        sort_order: str = 'asc',
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None,
        tag_group_id: str = None,
        search_text: str = None
    ) -> Dict:
        """Get the related FRED tags for one or more FRED tags within a category.

        ### Overview
        ----
        Optionally, filter results by tag group or search. FRED tags are attributes
        assigned to series. For this request, related FRED tags are the tags assigned
        to series that match all tags in the tag_names parameter, no tags in the
        exclude_tag_names parameter, and the category set by the category_id parameter.
        See the related request fred/category/tags. Series are assigned tags and
        categories. Indirectly through series, it is possible to get the tags for a
        category. No tags exist for a category that does not have series.

        ### Parameters
        ----
        category_id : str
            The category ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        order_by : str (optional, Default='series_count')
            Order results by values of the specified attribute. One of the
            following strings: ['series_count', 'popularity', 'created',
            'name', 'group_id'].

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match ALL of.Example value: ['income','bea'].
            See the related request: https://fred.stlouisfed.org/docs/api/fred/tags.html.

        exclude_tag_names : List[str] (optional, Default=None)
            A list of tag names that series match NONE of. Example value: ['income','bea'].
            See the related request: https://fred.stlouisfed.org/docs/api/fred/tags.html.

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen', 
            'geo', 'geot', 'rls', 'seas', 'src'].

        search_text : str (optional, Default=None)
            The words to find matching tags with.

        ### Returns
        ----
        Dict:
            A `Category` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> categories_service = fred_client.categories()
            >>> categories_service.get_category_tags(category_id='125')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/tags',
            params={
                'category_id': category_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'order_by': order_by,
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'sort_order': sort_order,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names,
                'tag_group_id': tag_group_id,
                'search_text': search_text
            }
        )

        return content
