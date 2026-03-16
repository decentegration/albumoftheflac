# Standard
from datetime import datetime


def parse_date(date: str) -> str:
    formats = ["%B %d, %Y", "%B %Y", "%Y"]

    for format in formats:
        try:
            date_object = datetime.strptime(date, format)

            if format == "%B %Y":
                date_object = date_object.replace(day=0)

            if format == "%Y":
                date_object = date_object.replace(day=0, month=0)

            return date_object.strftime("%Y-%m-%d")

        except ValueError:
            continue

    raise ValueError(f"Unrecognized date format: {date}")
