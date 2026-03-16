# Standard
from datetime import datetime

# Third party
from loguru import logger


def parse_date(date: str) -> str:
    logger.debug(f"raw date: {date}")

    date = date.replace("\xa0", " ")
    date = " ".join(date.split())
    date = date.strip()

    formats = ["%B %d, %Y", "%B %Y", "%Y"]

    for format in formats:
        try:
            date_object = datetime.strptime(date, format)

            if format == "%B %Y":
                date_object = date_object.replace(day=0)

            if format == "%Y":
                date_object = date_object.replace(day=0, month=0)

            formatted_date = date_object.strftime("%Y-%m-%d")
            logger.debug(f"formatted date: {formatted_date}")
            return formatted_date

        except ValueError:
            continue

    raise ValueError(f"Unrecognized date format: {date}")
