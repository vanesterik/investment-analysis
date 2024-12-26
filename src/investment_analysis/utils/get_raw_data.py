from typing import Optional

from investment_analysis.utils.request_url import request_url


def get_raw_data(symbol: str, start_date: str, end_date: str) -> str:
    """
    Get raw data from the FT API for a given symbol and date range.

    Parameters
    ----------
    - symbol (str): The symbol to get data for.
    - start_date (str): The start date of the data range.
    - end_date (str): The end date of the data range.

    Returns
    -------
    - Optional[str]: The raw data if successful, None otherwise

    """

    base_url = "https://markets.ft.com/data/equities/ajax/get-historical-prices"
    query_params = f"?startDate={start_date}&endDate={end_date}&symbol={symbol}"
    content = request_url(base_url + query_params)

    return content if content is not None else '{"data":{},"html":{}'
