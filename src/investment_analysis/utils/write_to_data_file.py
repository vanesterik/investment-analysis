from pathlib import Path


def write_to_data_file(filepath: str, data: str) -> None:
    """
    Write data to filepath in the data directory.

    Parameters
    ----------
    - filepath (Path): The path to the file to write the data to.
    - data (str): The data to write to the file.

    """

    # Define base path for all data files
    data_dir = Path("data")

    # Write data to file
    with open(data_dir / filepath, "w") as file:
        file.write(data)
