from datetime import date

import click
from halo import Halo

from investment_analysis.data.get_fred_data import get_fred_data
from investment_analysis.data.get_ft_data import get_ft_data
from investment_analysis.utils.write_to_data_file import write_to_data_file


@click.command()
@click.argument(
    "start_date",
    default="1985/01/01",
    type=click.STRING,
)
@click.argument(
    "end_date",
    default=date.today().strftime("%Y/%m/%d"),
    type=click.STRING,
)
def main(start_date: str, end_date: str) -> None:

    spinner = Halo(
        color="white",
        placement="right",
        spinner="simpleDots",
        text="Getting and processing data",
    )
    spinner.start()

    # Get and process FT data
    symbols = [
        "127714196",  # ING ARIA - ING Global Index Portfolio Dynamic B EUR Acc
    ]

    for symbol in symbols:
        data = get_ft_data(
            symbol,
            start_date,
            end_date,
        )
        write_to_data_file(f"{symbol}.csv", data)

    # Get and process FRED data
    ids = [
        "DGS2",  # 2-Year Treasury Constant Maturity Rate
        "DGS10",  # 10-Year Treasury Constant Maturity Rate
    ]

    for id in ids:
        data = get_fred_data(
            id,
            start_date.replace("/", "-"),
            end_date.replace("/", "-"),
        )
        write_to_data_file(f"{id}.csv", data)

    spinner.stop()


if __name__ == "__main__":
    main()
