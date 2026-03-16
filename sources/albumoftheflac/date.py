# Standard
from datetime import datetime

# Third party
from loguru import logger


def parse_date(date: str) -> str:
    logger.debug(f"raw date: {date}")

    date = date.replace("\xa0", " ")
    date = " ".join(date.split())
    date = date.strip()

    formats = [("%B %d, %Y", "%Y-%m-%d"), ("%B %Y", "%Y-%m"), ("%Y", "%Y")]

    for input_format, output_format in formats:
        try:
            date_object = datetime.strptime(date, input_format)
            formatted_date = date_object.strftime(output_format)
            logger.debug(f"formatted date: {formatted_date}")
            return formatted_date

        except ValueError:
            continue

    raise ValueError(f"Unrecognized date format: {date}")
