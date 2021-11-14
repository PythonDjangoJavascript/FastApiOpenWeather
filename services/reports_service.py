import uuid
from datetime import datetime
from typing import List
from models.location import Location

from models.report import Report


# its a representative of database model
__reports: List[Report] = []


# retrieve all inputed report data
def get_report() -> List[Report]:
    return list(__reports)


def add_report(description: str, location: Location) -> Report:
    """add a report to the database and returns it"""
    report = Report(
        id=str(uuid.uuid4()),
        description=description,
        location=location,
        created_at=str(datetime.now())
    )

    __reports.append(report)
    __reports.sort(key=lambda rep: rep.created_at, reverse=True)

    return report
