from datetime import date

import click

from investment_analysis.utils.get_raw_data import get_raw_data
from investment_analysis.utils.process_interim_data import process_interim_data
from investment_analysis.utils.process_raw_data import process_raw_data
from investment_analysis.utils.write_to_data_file import write_to_data_file


@click.command()
@click.argument("symbol", type=click.STRING, default="127714196")
@click.argument("start_date", type=click.STRING, default="2019/01/01")
@click.argument(
    "end_date", type=click.STRING, default=date.today().strftime("%Y/%m/%d")
)
def main(symbol: str, start_date: str, end_date: str) -> None:

    # Get raw data
    raw_data = get_raw_data(symbol, start_date, end_date)
    write_to_data_file(f"raw/{symbol}.json", raw_data)

    # Process raw data
    html_data = process_raw_data(raw_data)
    write_to_data_file(f"interim/{symbol}.html", html_data)

    # Process interim data
    data = process_interim_data(html_data)
    write_to_data_file(f"processed/{symbol}.csv", data)


if __name__ == "__main__":
    main()
