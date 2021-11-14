import datetime
from typing import Optional
from pydantic import BaseModel

from models.location import Location


class ReportSubmittal(BaseModel):
    """Reqport submittal base model"""
    description: str
    location: Location


class Report(ReportSubmittal):
    """Create Report Pydantic Model"""
    id: str
    created_at: Optional[datetime.datetime]
