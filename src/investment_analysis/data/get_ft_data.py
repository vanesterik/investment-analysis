import json
from typing import Dict

from bs4 import BeautifulSoup

from investment_analysis.constants import feature_names as fn
from investment_analysis.utils.parse_to_timestamp import parse_to_timestamp
from investment_analysis.utils.request_url import request_url


def get_ft_data(symbol: str, start_date: str, end_date: str) -> str:
    """
    Get and process data from the FT API for a given symbol and date range.

    Parameters
    ----------
    - symbol (str): The symbol to get data for.
    - start_date (str): The start date of the data range.
    - end_date (str): The end date of the data range.

    Returns
    -------
    - str: The processed data in csv format.

    """

    # Get raw data from the FT API
    base_url = "https://markets.ft.com/data/equities/ajax/get-historical-prices"
    query_params = f"?startDate={start_date}&endDate={end_date}&symbol={symbol}"
    content = request_url(base_url + query_params)

    # Define empty json structure if no content
    content = content if content is not None else '{"data":{},"html":{}}'

    # Convert raw data to JSON and type to Dict
    json_data: Dict[str, str] = json.loads(content)

    # Define html data
    html_data = json_data["html"]

    # Process HTML data
    soup = BeautifulSoup(html_data, "html.parser")
    rows = soup.find_all("tr")
    data = []

    # Iterate over each row and extract relevant data to data list
    for row in rows:
        cols = row.find_all("td")

        # Define timestamp based on date string
        timestamp = parse_to_timestamp(cols[0].find_all("span")[0].text)

        # Extract data and append to data list
        data.append(
            [
                timestamp,
                float(cols[1].text),
                float(cols[2].text),
                float(cols[3].text),
                float(cols[4].text),
                float(cols[5].find_all("span")[0].text.replace(",", "")),
            ]
        )

    # Define the header row
    header = (
        ",".join([fn.TIMESTAMP, fn.OPEN, fn.HIGH, fn.LOW, fn.CLOSE, fn.VOLUME])
        + "\n"
    )

    # Reverse data list to have ascending order of timestamps
    data = data[::-1]

    # Flatten the data list and convert to csv format
    content = "\n".join([",".join(map(str, row)) for row in data])

    # Return the header and content
    return str(header + content)
