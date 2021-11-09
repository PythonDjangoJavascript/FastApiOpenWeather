from typing import Optional
from fastapi import Depends
from fastapi.routing import APIRouter

from models.location import Location
from services.open_weather_service import get_weather_api


router = APIRouter()


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):

    report = get_weather_api(loc.city, loc.state, loc.country, units=units)

    return report
