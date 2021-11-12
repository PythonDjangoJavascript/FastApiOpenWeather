import datetime
from typing import Optional
from pydantic import BaseModel

from models.location import Location


class Report(BaseModel):
    """Create Report Pydantic Model"""
    description: str
    location: Location
    created_at: Optional[datetime.datetime]
