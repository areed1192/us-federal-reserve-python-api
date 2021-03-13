from typing import Dict
from typing import List
from typing import Union
from datetime import datetime
from fred.session import FredSession

# Used for type hinting
todays_date = datetime.today().date().isoformat()


class Series():

    """
    ## Overview:
    ----
    The Federal Reserve offers a wide variety of data including
    series data. Series Data is used for different types of analysis
    in economics. This Service will help you capture different series
    data nad metadata associated with it.
    """

    def __init__(self, session: FredSession) -> None:
        """Initializes the `Series` object.

        ### Parameters
        ----
        session : `FredSession`
            An initialized session of the `FredSession`.
        """

        # Set the session.
        self.fred_session: FredSession = session

        # Set the endpoint.
        self.endpoint = '/series'
        self._todays_date = datetime.today().date().isoformat()

    def __repr__(self) -> str:
        """String representation of the `FederalReserveClient.Series` object."""

        # define the string representation
        str_representation = '<FederalReserveClient.Series (active=True, connected=True)>'

        return str_representation

    def get_series(
        self,
        series_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date
    ) -> Dict:
        """Get an economic data series.

        ### Parameters
        ----------
        series_id : str
            The series ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series(series_id='GNPCA')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint,
            params={
                'series_id': series_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end
            }
        )

        return content

    def get_series_categories(
        self,
        series_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date
    ) -> Dict:
        """Get the categories for an economic data series.

        ### Parameters
        ----------
        series_id : str
            The series ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series_categories(series_id='EXJPUS')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/categories',
            params={
                'series_id': series_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end
            }
        )

        return content

    def get_series_observations(
        self,
        series_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        observation_start: Union[str, datetime] = '1776-07-04',
        observation_end: Union[str, datetime] = '9999-12-31',
        units: str = 'lin',
        frequency: str = None,
        aggregation_method: str = 'avg',
        output_type: int = 1,
        vintage_dates: Union[List[str], List[datetime]] = None
    ) -> Dict:
        """Get the observations or data values for an economic data series.

        ### Parameters
        ----------
        series_id : str
            The series ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        observation_start : Union[str, datetime] (optional, Default='1776-07-04')
            The start of the observation period. YYYY-MM-DD formatted string.

        observation_end : Union[str, datetime] (optional, Default='9999-12-31')
            The end of the observation period. YYYY-MM-DD formatted string.

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        sort_order : str
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].
            optional, default: `asc`.

        units : str (optional, Default='lin')
            A key that indicates a data value transformation. One of the following
            values: ['lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log']
            For unit transformation formulas, see: https://alfred.stlouisfed.org/help#growth_formulas

        frequency : str (optional, Default=None)
            An optional parameter that indicates a lower frequency to aggregate values to.
            One of the following values: ['d', 'w', 'bw', 'm', 'q', 'sa', 'a', 'wef', 'weth',
            'wew', 'wetu', 'wem', 'wesu','wesa', 'bwew', 'bwem'] For more info,
            see: https://fred.stlouisfed.org/docs/api/fred/series_observations.html

        aggregation_method : str (optional, Default='avg')
            A key that indicates the aggregation method used for frequency aggregation.
            This parameter has no affect if the frequency parameter is not set. One of 
            the following values: ['avg', 'sum', 'eop']

        output_type : int (optional, Default=1)
            An integer that indicates an output type. One of the following values:
            ['1', '2', '3', '4'].
            1 = Observations by Real-Time Period
            2 = Observations by Vintage Date, All Observations
            3 = Observations by Vintage Date, New and Revised Observations Only
            4 = Observations, Initial Release Only

        vintage_dates : Union[List[str], List[datetime]] (optional, Default=None)
            A comma separated string of YYYY-MM-DD formatted dates in history (e.g. 2000-01-01,2005-02-24).
            Vintage dates are used to download data as it existed on these specified dates in history.
            Vintage dates can be specified instead of a real-time period using realtime_start and
            realtime_end.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series_observations(series_id='GNPCA')
        """

        # Conver the date to proper formats.
        if vintage_dates:
            iso_dates = []
            for date in vintage_dates:
                if isinstance(date, datetime):
                    iso_dates.append(date.date().isoformat())
                else:
                    iso_dates.append(iso_dates)

            vintage_dates = ','.join(vintage_dates)

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/observations',
            params={
                'series_id': series_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'observation_start': observation_start,
                'observation_end': observation_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'units': units,
                'frequency': frequency,
                'aggregation_method': aggregation_method,
                'output_type': output_type,
                'vintage_dates': vintage_dates
            }
        )

        return content

    def get_series_release(
        self,
        series_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date
    ) -> Dict:
        """Get the release for an economic data series.

        ### Parameters
        ----------
        series_id : str
            The series ID you want to query.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series_release(series_id='IRA')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/release',
            params={
                'series_id': series_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end
            }
        )

        return content

    def series_search(
        self,
        search_text: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'series_id',
        search_type: str = 'full_text',
        filter_variable: str = None,
        filter_value: str = None,
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None
    ) -> Dict:
        """Get economic data series that match search text.

        ### Parameters
        ----------
        search_text : str
            The words to match against economic data series.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        observation_start : Union[str, datetime] (optional, Default='1776-07-04')
            The start of the observation period. YYYY-MM-DD formatted string.

        observation_end : Union[str, datetime] (optional, Default='9999-12-31')
            The end of the observation period. YYYY-MM-DD formatted string.

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        order_by : str (optional, Default=Union['series_id', 'search_rank'])
            One of the following strings: ['search_rank', 'series_id', 'title', 
            'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 
            'last_updated', 'observation_start', 'observation_end', 'popularity',
            'group_popularity']

        search_type : str (optional, Default='full_text')
            Determines the type of search to perform. One of the following strings:
            ['full_text', 'series_id']. 'full_text' searches series attributes title,
            units, frequency, and tags by parsing words into stems. 'series_id' performs
            a substring search on series IDs. 

        filter_variable : str (optional, Default=None)
            The attribute to filter results by. One of the following strings: 
            ['frequency', 'units', 'seasonal_adjustment'].

        filter_value : str (optional, Default=None)
            The value of the filter_variable attribute to filter results by.

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match all of.

        exclude_tag_names : List[str] (optional, Default=None)
            A list of tag names that series match None of. Parameter exclude_tag_names 
            requires that parameter tag_names also be set to limit the number of 
            matching series.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.series_search(search_text='Monetary Service Index')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/search',
            params={
                'search_text': search_text,
                'search_type': search_type,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'order_by': order_by,
                'filter_variable': filter_variable,
                'filter_value': filter_value,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names,
            }
        )

        return content

    def series_tag_search(
        self,
        series_search_text: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'series_count',
        tag_group_id: str = None,
        tag_search_text: str = None,
        tag_names: List[str] = None,
    ) -> Dict:
        """Get the FRED tags for a series search. Optionally,
        filter results by tag name, tag group, or tag search.
        See the related request fred/series/search/related_tags.

        ### Parameters
        ----------
        search_text : str
            The words to match against economic data series.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        observation_start : Union[str, datetime] (optional, Default='1776-07-04')
            The start of the observation period. YYYY-MM-DD formatted string.

        observation_end : Union[str, datetime] (optional, Default='9999-12-31')
            The end of the observation period. YYYY-MM-DD formatted string.

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        order_by : str (optional, Default=Union['series_id', 'search_rank'])
            One of the following strings: ['series_count', 'popularity', 'created',
            'name', 'group_id']

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen',
            'geo', 'geot', 'rls', 'seas', 'src'].

        tag_search_text : str (optional, Default=None)
            The words to find matching tags with.

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match all of.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.series_tag_search(series_search_text='Monetary Service Index')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/search/tags',
            params={
                'series_search_text': series_search_text,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'order_by': order_by,
                'tag_group_id': tag_group_id,
                'tag_search_text': tag_search_text,
                'tag_names': tag_names,
            }
        )

        return content

    def series_releated_tags_search(
        self,
        series_search_text: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
        order_by: str = 'series_count',
        tag_group_id: str = None,
        tag_search_text: str = None,
        tag_names: List[str] = None,
        exclude_tag_names: List[str] = None,
    ) -> Dict:
        """Get the FRED tags for a series search. Optionally,
        filter results by tag name, tag group, or tag search.
        See the related request fred/series/search/related_tags.

        ### Parameters
        ----------
        search_text : str
            The words to match against economic data series.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        observation_start : Union[str, datetime] (optional, Default='1776-07-04')
            The start of the observation period. YYYY-MM-DD formatted string.

        observation_end : Union[str, datetime] (optional, Default='9999-12-31')
            The end of the observation period. YYYY-MM-DD formatted string.

        offset : int (optional, Default=0)
            Non-negative integer.

        limit : int (optional, Default=1000)
            The maximum number of results to return. Is an integer
            between 1 and 1000.

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        order_by : str (optional, Default=Union['series_id', 'search_rank'])
            One of the following strings: ['series_count', 'popularity', 'created',
            'name', 'group_id']

        tag_group_id : str (optional, Default=None)
            A tag group id to filter tags by type. One of the following: ['freq', 'gen',
            'geo', 'geot', 'rls', 'seas', 'src'].

        tag_search_text : str (optional, Default=None)
            The words to find matching tags with.

        tag_names : List[str] (optional, Default=None)
            A list of tag names that series match all of.

        exclude_tag_names : List[str] (optional, Default=None)
            A list of tag names that series match None of. Parameter exclude_tag_names 
            requires that parameter tag_names also be set to limit the number of 
            matching series.

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.series_releated_tags_search(
                    series_search_text='Mortgage Rates',
                    tag_names=['30-year', 'frb']
                )
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/search/related_tags',
            params={
                'series_search_text': series_search_text,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
                'order_by': order_by,
                'tag_group_id': tag_group_id,
                'tag_search_text': tag_search_text,
                'tag_names': tag_names,
                'exclude_tag_names': exclude_tag_names
            }
        )

        return content

    def get_series_tags(
        self,
        series_id: str,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        sort_order: str = 'asc',
        order_by: str = 'series_count',
    ) -> Dict:
        """Get the FRED tags for a series.

        ### Parameters
        ----------
        series_id : str
            The ID for a series.

        realtime_start : Union[str, datetime] (optional, Default=today's date)
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default=today's date)
            The end of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        sort_order : str (optional, Default='asc')
            Sort results is ascending or descending order for attribute values
            specified by order_by. One of the following strings: ['asc', 'desc'].

        order_by : str (optional, Default='series_count')
            One of the following strings: ['series_count', 'popularity', 'created',
            'name', 'group_id']

        ### Returns
        -------
        Dict
            A collection of `Series.Tags` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series_tags(series_id='STLFSI')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/tags',
            params={
                'series_id': series_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'sort_order': sort_order,
                'order_by': order_by,
            }
        )

        return content

    def get_series_updates(
        self,
        realtime_start: Union[str, datetime] = todays_date,
        realtime_end: Union[str, datetime] = todays_date,
        offset: int = 0,
        limit: int = 1000,
        filter_value: str = 'all',
        start_time: str = None,
        end_time: str = None
    ) -> Dict:
        """Get economic data series sorted by when observations were updated on the 
        FRED® server (attribute last_updated). Results are limited to series updated
        within the last two weeks.

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

        filter_value : str (optional, Default='all')
            Limit results by geographic type of economic data series; 
            namely 'macro', 'regional', and 'all'.

        start_time: str (optional, Default=None)
            Start time for limiting results for a time range, can filter 
            down to minutes. YYYYMMDDHhmm formatted string end_time is 
            required if start_time is set

        end_time: str (optional, Default=None)
            End time for limiting results for a time range, can filter 
            down to minutes. YYYYMMDDHhmm formatted string start_time is 
            required if end_time is set

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series_updates()
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/updates',
            params={
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'filter_value': filter_value,
                'start_time': start_time,
                'end_time': end_time
            }
        )

        return content

    def get_series_vintage_dates(
        self,
        series_id: str,
        realtime_start: Union[str, datetime] = '1776-07-04',
        realtime_end: Union[str, datetime] = '9999-12-31',
        offset: int = 0,
        limit: int = 1000,
        sort_order: str = 'asc',
    ) -> Dict:
        """Get the dates in history when a series' data values were revised or 
        new data values were released. Vintage dates are the release dates for
        a series excluding release dates when the data for the series did not
        change.

        ### Parameters
        ----------
        series_id : str
            The ID for a series.

        realtime_start : Union[str, datetime] (optional, Default='1776-07-04')
            The start of the real-time period. For more information, see 
            Real-Time Periods. YYYY-MM-DD formatted string.

        realtime_end : Union[str, datetime] (optional, Default='9999-12-31')
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

        ### Returns
        -------
        Dict
            A collection of `Series` resources.

        ### Usage
        ----
            >>> fred_client = FederalReserveClient(api_key='xxxxxx')
            >>> series_service = fred_client.series()
            >>> series_service.get_series_vintage_dates(series_id='GNPCA')
        """

        content = self.fred_session.make_request(
            method='get',
            endpoint=self.endpoint + '/vintagedates',
            params={
                'series_id': series_id,
                'api_key': self.fred_session.client._api_key,
                'file_type': 'json',
                'realtime_start': realtime_start,
                'realtime_end': realtime_end,
                'offset': offset,
                'limit': limit,
                'sort_order': sort_order,
            }
        )

        return content
