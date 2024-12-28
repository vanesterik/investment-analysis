from bs4 import BeautifulSoup

from investment_analysis.constants import feature_names as fn
from investment_analysis.utils.parse_to_timestamp import parse_to_timestamp


def process_interim_data(html_data: str) -> str:
    """
    Process the HTML data to extract the relevant information.

    Parameters
    ----------
    - html_data (str): The HTML data to process.

    Returns
    -------
    - str: The processed data in csv format.

    """

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
    return header + content
