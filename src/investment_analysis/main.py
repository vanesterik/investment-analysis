from datetime import date
from typing import List

import click
from halo import Halo

from investment_analysis.data.get_raw_data import get_raw_data
from investment_analysis.data.process_interim_data import process_interim_data
from investment_analysis.data.process_raw_data import process_raw_data
from investment_analysis.utils.write_to_data_file import write_to_data_file


@click.command()
@click.argument(
    "start_date",
    default="2019/01/01",
    type=click.STRING,
)
@click.argument(
    "end_date",
    default=date.today().strftime("%Y/%m/%d"),
    type=click.STRING,
)
@click.option(
    "--symbols",
    default=[
        "127714196",  # ING ARIA - ING Global Index Portfolio Dynamic B EUR Acc
    ],
    multiple=True,
    type=click.STRING,
)
def main(start_date: str, end_date: str, symbols: List[str]) -> None:

    spinner = Halo(
        color="white",
        placement="right",
        spinner="simpleDots",
        text="Getting and processing data",
    )
    spinner.start()

    for symbol in symbols:

        raw_data = get_raw_data(symbol, start_date, end_date)
        write_to_data_file(f"raw/{symbol}.json", raw_data)

        html_data = process_raw_data(raw_data)
        write_to_data_file(f"interim/{symbol}.html", html_data)

        data = process_interim_data(html_data)
        write_to_data_file(f"processed/{symbol}.csv", data)

    spinner.stop()


if __name__ == "__main__":
    main()
