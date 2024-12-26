import json
from typing import Dict


def process_raw_data(raw_data: str) -> str:
    """
    Process raw data to extract HTML data.

    Parameters
    ----------
    - raw_data (str): The raw data to process.

    Returns
    -------
    - str: The extracted HTML data.

    """

    # Convert raw data to JSON and type to Dict
    json_data: Dict[str, str] = json.loads(raw_data)

    # Return the HTML data
    return json_data["html"]
