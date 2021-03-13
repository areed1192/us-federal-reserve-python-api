from typing import Dict
from typing import List
from typing import Union
from datetime import datetime
from fred.session import FredSession

# Used for type hinting
todays_date = datetime.today().date().isoformat()


class Releases():

    """
    ## Overview:
    ----
    Releases are economic data provided by the United States
    Federal Reserve in the form of economic reports. The Releases
    services allows you to query and search for Releases using the
    FRED API.
    """

    def __init__(self, session: FredSession) -> None:
        """Initializes the `Releases` object.

        ### Parameters
        ----
        session : `FredSession`
            An initialized session of the `FredSession`.
        """

        # Set the session.
        self.fred_session: FredSession = session

        # Set the endpoint.
        self.endpoint = '/release'
        self.endpoint_collection = '/releases'
        self._todays_date = datetime.today().date().isoformat()

    def __repr__(self) -> str:
        """String representation of the `FederalReserveClient.Releases` object."""

        # define the string representation
        str_representation = '<FederalReserveClient.Releases (active=True, connected=True)>'

        return str_representation

    def get_releases(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        order_by: str = 'release_id',
        sort_order: str = 'asc'
    ) -> Dict:
        """Get the series in a category.

        ### Parameters
        ----

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        offset : int
            Non-negative integer, optional, default: 0.

        limit : int
            The maximum number of results to return. Is an integer
            between 1 and 1000, optional, default: 1000

        order_by : str
            One of the following strings: ['release_id', 'name', 
            'press_release', 'realtime_start', 'realtime_end'].
            optional, default: release_id

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service = fred_client.get_releases()
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint_collection,
            params={
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'order_by': order_by,
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'sort_order': sort_order
            }
        )

        return content

    def get_releases_dates(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        order_by: str = 'release_date',
        sort_order: str = 'asc'
    ) -> Dict:
        """Get release dates for all releases of economic data.

        ### Parameters
        ----

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        offset : int
            Non-negative integer, optional, default: 0.

        limit : int
            The maximum number of results to return. Is an integer
            between 1 and 1000, optional, default: 1000

        order_by : str
            One of the following strings: ['release_date', 'release_id',
             'release_name']. optional, default: release_date

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_releases_dates()
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint_collection,
            params={
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'order_by': order_by,
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'sort_order': sort_order
            }
        )

        return content

    def get_release_by_id(
        self,
        release_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
    ) -> Dict:
        """Get release dates for all releases of economic data.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_by_id(release_id='53')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint,
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
            }
        )

        return content

    def get_release_dates(
        self,
        release_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        include_release_dates_with_no_data: bool = False
    ) -> Dict:
        """Get release dates for a release of economic data.

        ### Overview:
        ----
        Note that release dates are published by data sources
        and do not necessarily represent when data will be
        available on the FRED or ALFRED websites.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        offset : int
            Non-negative integer, optional, default: 0.

        limit : int
            The maximum number of results to return. Is an integer
            between 1 and 1000, optional, default: 1000

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        include_release_dates_with_no_data : bool
            Determines whether release dates with no data available are returned.
            The defalut value 'false' excludes release dates that do not have data.
            In particular, this excludes future release dates which may be available
            in the FRED release calendar or the ALFRED release calendar. One of the
            following strings: ['true', 'false']. optional, default: false

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_by_id(release_id='53')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/dates',
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'limit': limit,
                'offset': offset,
                'sort_order': sort_order,
                'include_release_dates_with_no_data': str(include_release_dates_with_no_data).lower()
            }
        )

        return content

    def get_release_series(
        self,
        release_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        filter_variable: str = None,
        filter_value: str = None,
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None
    ) -> Dict:
        """Get the series on a release of economic data.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        offset : int
            Non-negative integer, optional, default: 0.

        limit : int
            The maximum number of results to return. Is an integer
            between 1 and 1000, optional, default: 1000

        order_by : str
            One of the following strings: ['release_date', 'release_id',
             'release_name']. optional, default: release_date

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        filter_variable : str
            The attribute to filter results by. On of the following strings:
            ['frequency', 'units', 'seasonal_adjustment']. optional, no filter
            by default

        filter_value : str
            The value of the filter_variable attribute to filter results by.
            optional, no filter by default.

        tag_names : List[str]
            A list of tag names that series match ALL of. Example value: ['japan', 'imports'].
            optional, no filtering by tags by default See the related request:
            https://fred.stlouisfed.org/docs/api/fred/tags.html.

        exclude_tag_names : List[str]
            A list of tag names that series match NONE of. Example value: ['japan', 'imports'].
            optional, no filtering by tags by default See the related request:
            https://fred.stlouisfed.org/docs/api/fred/tags.html.

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_series(release_id='53')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/series',
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
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

    def get_release_sources(
        self,
        release_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
    ) -> Dict:
        """Get the sources for a release of economic data.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_sources(release_id='51')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/sources',
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end
            }
        )

        return content

    def get_release_tags(
        self,
        release_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        search_text: str = None,
        tag_group_id: List[str] = None,
        tag_names: List[str] = None,
        order_by: str = 'series_count'
    ) -> Dict:
        """Get the FRED tags for a release. Optionally, filter results 
        by tag name, tag group, or search. 

        ### Overview:
        ----
        Series are assigned tags and releases. Indirectly through series,
        it is possible to get the tags for a release. See the related 
        request fred/release/related_tags.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        offset : int
            Non-negative integer, optional, default: 0.

        limit : int
            The maximum number of results to return. Is an integer
            between 1 and 1000, optional, default: 1000

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        tag_names : List[str]
            A list of tag names that series match ALL of. Example value: ['japan', 'imports'].
            optional, no filtering by tags by default See the related request:
            https://fred.stlouisfed.org/docs/api/fred/tags.html.

        tag_group_id : str
            A tag group id to filter tags by type. String, optional, no filtering
            by tag group by default. One of the following: ['freq', 'gen', 'geo',
            'geot', 'rls', 'seas', 'src'].

        search_text : str
            The words to find matching tags with. Optional, no filtering by search
            words by default.

        order_by : str
            Order results by values of the specified attribute. One of the following
            strings: ['series_count', 'popularity', 'created', 'name', 'group_id'].
            optional, default: series_count

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_tags(release_id='86')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/tags',
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'search_text': search_text,
                'tag_names': tag_names,
                'tag_group_id': tag_group_id,
                'order_by': order_by
            }
        )

        return content

    def get_release_related_tags(
        self,
        release_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        search_text: str = None,
        tag_group_id: List[str] = None,
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None,
        order_by: str = 'series_count'
    ) -> Dict:
        """Get the related FRED tags for one or more FRED tags within a release.
        Optionally, filter results by tag group or search.

        ### Overivew:
        ----
        FRED tags are attributes assigned to series. For this request, related FRED
        tags are the tags assigned to series that match all tags in the tag_names
        parameter, no tags in the exclude_tag_names parameter, and the release set
        by the release_id parameter. See the related request fred/release/tags.
        Series are assigned tags and releases. Indirectly through series, it is 
        possible to get the tags for a release.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        realtime_start : Union[str, datetime]
            The start of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        realtime_end : Union[str, datetime]
            The end of the real-time period. For more information,
            see Real-Time Periods. YYYY-MM-DD formatted string,
            optional, default: today's date

        offset : int
            Non-negative integer, optional, default: 0.

        limit : int
            The maximum number of results to return. Is an integer
            between 1 and 1000, optional, default: 1000

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        tag_names : List[str]
            A list of tag names that series match ALL of. Example value: ['japan', 'imports'].
            optional, no filtering by tags by default See the related request:
            https://fred.stlouisfed.org/docs/api/fred/tags.html.

        exclude_tag_names : List[str]
            A semicolon delimited list of tag names that series match none of. String, optional,
            no default value. Example value: ['monthly, financial'].

        tag_group_id : str
            A tag group id to filter tags by type. String, optional, no filtering
            by tag group by default. One of the following: ['freq', 'gen', 'geo',
            'geot', 'rls', 'seas', 'src'].

        search_text : str
            The words to find matching tags with. Optional, no filtering by search
            words by default.

        order_by : str
            Order results by values of the specified attribute. One of the following
            strings:  'series_count', 'popularity', 'created', 'name', 'group_id'].
            optional, default: series_count

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_related_tags(release_id='86')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/tags',
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'search_text': search_text,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names,
                'tag_group_id': tag_group_id,
                'order_by': order_by
            }
        )

        return content

    def get_release_tables(
        self,
        release_id: str,
        element_id: int = None,
        include_observations_value: bool = False,
        observation_date: Union[str, datetime] = '9999-12-31'
    ) -> Dict:
        """Get the related FRED tags for one or more FRED tags within a release.
        Optionally, filter results by tag group or search.

        ### Overivew:
        ----
        FRED tags are attributes assigned to series. For this request, related FRED
        tags are the tags assigned to series that match all tags in the tag_names
        parameter, no tags in the exclude_tag_names parameter, and the release set
        by the release_id parameter. See the related request fred/release/tags.
        Series are assigned tags and releases. Indirectly through series, it is 
        possible to get the tags for a release.

        ### Parameters
        ----

        release_id : str
            The release ID you want to query.

        element_id : int (optional, Default=None)
            The release table element id you would like to
            retrieve. When the parameter is not passed, the 
            root(top most) element for the release is given.

        include_observation_values : bool (optional, Default=False)
            A flag to indicate that observations need to be returned.
            Observation value and date will only be returned for a series
            type element. One of the following strings: [True, False].

        observation_date: Union[str, datetime] (optional, Default='9999-12-31')
                The observation date to be included with the returned
                release table. YYYY-MM-DD formatted string.

        ### Returns
        ----
        Dict:
            A `Releases` Collection Resource Object.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> releases_service = fred_client.releases()
            >>> releases_service.get_release_related_tables(release_id='53')
        """

        if isinstance(observation_date, datetime):
            observation_date = observation_date.isoformat()

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/tables',
            params={
                'release_id': release_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'element_id': element_id,
                'include_observations_value': str(include_observations_value).lower(),
                'observation_date': observation_date
            }
        )

        return content
