from investment_analysis.utils.request_url import request_url


def get_fred_data(id: str, start_date: str, end_date: str) -> str:
    """
    Get raw data from the FRED API for a given id and date range.

    Parameters
    ----------
    - id (str): The id to get data for.
    - start_date (str): The start date of the data range.
    - end_date (str): The end date of the data range.

    Returns
    -------
    - str: The raw data from the FRED API.

    """

    base_url = "https://fred.stlouisfed.org/graph/fredgraph.csv"
    query_params = f"?id={id}&cosd={start_date}&coed={end_date}"
    content = request_url(base_url + query_params)

    if content is None:
        return ""

    return str(content)
