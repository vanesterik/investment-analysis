from typing import Optional

import requests


def request_url(url: str, timeout: int = 10) -> Optional[str]:
    """
    Request content from a URL.

    Parameters
    ----------
    - url (str): The URL to request.
    - timeout (int): The timeout for the request in seconds. Defaults to 10.

    Returns
    -------
    - Optional[str]: The content of the URL if successful, None otherwise.

    """

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text

    except requests.RequestException as e:
        print(f"Error requesting URL '{url}': {e}")
        return None
