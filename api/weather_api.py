from typing import List, Optional
from fastapi import Depends, Response, status
from fastapi.routing import APIRouter
import httpx

from models.location import Location
from models.report import Report
from models.validation_error import ValidationError
from services.open_weather_service import get_weather_api_async
from services import reports_service


router = APIRouter()


# Asyncronasly calling the method
@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):

    try:
        return await get_weather_api_async(loc.city, loc.state, loc.country, units=units)
    except ValidationError as ve:
        return Response(content=ve.error_message, status_code=ve.status_code)
    except httpx.ConnectError as ce:
        print(ce.args)
        return Response(content="Unable to connect, Please check your network", status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"Server Crashed while processing request: {e}")
        return Response(content="Error Processing your request", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/api/reports', name='all_reports')
def get_report() -> List[Report]:
    """Get all added reports data"""
    reports_service.add_report("Hello", Location(city="Dhaka"))
    reports_service.add_report("World", Location(city="Portland"))

    return reports_service.get_report()
