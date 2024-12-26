from datetime import datetime


def parse_to_timestamp(date_str: str, format_str: str = "%A, %B %d, %Y") -> int:
    """
    Convert a date string to a Unix timestamp in milliseconds.

    Parameters
    ----------
    - date_str (str): The date string to convert.
    - format_str (str): The format of the date string. Defaults to '%A, %B %d, %Y'.

    Returns
    -------
    - int: The Unix timestamp in milliseconds

    """

    date = datetime.strptime(date_str, format_str)
    return int(date.timestamp() * 1000)
