from typing import Optional
from pydantic import BaseModel


class Location(BaseModel):
    """Create location pydantic basmodel"""

    city: str
    state: Optional[str] = None
    country: Optional[str] = 'US'
