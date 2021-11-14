import requests
import httpx
from typing import Optional, Tuple

from starlette import status

from infrastructure import weather_chache
from models.validation_error import ValidationError


api_key: Optional[str] = None


async def get_weather_api_async(city: str, state: Optional[str], country: Optional[str], units: str) -> dict:

    # validate all units
    city, state, country, units = validate_units(city, state, country, units)

    # TODO: check woras oparator... example ->
    if forcast := weather_chache.get_weather(city, state, country, units):
        return forcast

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"

    # url = f"api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}"

    # Now send the async request
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        # response.raise_for_status()  # will throw an exception if status goes wrong

        # if error occure while requesting for response
        if response.status_code != 200:
            raise ValidationError(response.text, response.status_code)

    data = response.json()
    forcast = data['main']  # filtering only main data

    # cache the data to show next time without hitting the exernal api
    weather_chache.set_weather(city, state, country, units, forcast)

    return forcast


# def get_weather_api(city: str, state: Optional[str], country: Optional[str], units: str) -> dict:

#     if state:
#         q = f"{city},{state},{country}"
#     else:
#         q = f"{city},{country}"

#     # url = f"api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}"

#     # now send a get request
#     response = requests.get(url)
#     response.raise_for_status()  # will throw an exception if status goes wrong

#     data = response.json()
#     print(data)

#     return data


def validate_units(city: str, state: Optional[str], coutnry: Optional[str], units: str) \
        -> Tuple[str, Optional[str], str, str]:
    """Validate all units"""

    # validate city
    city = city.lower().strip()

    # validate country
    if not coutnry:
        coutnry = 'US'
    else:
        coutnry = coutnry.lower().strip()

    if len(coutnry) != 2:
        error = f"Invalid countyr: {coutnry}. It must be two letter abbreviation such as US or UK"
        raise ValidationError(error_message=error,
                              status_code=status.HTTP_400_BAD_REQUEST)

    # validate state
    if state:
        state = state.lower().strip()
    if state and len(state) != 2:
        error = f"Invalid state: {state}. It must be two letters abbreviation"
        raise ValidationError(error, status.HTTP_400_BAD_REQUEST)

    # validate units
    if units:
        units = units.strip().lower()
    valid_units = {'standard', 'metric', 'imperial'}
    if units not in valid_units:
        error = f"Invalid Units '{units}', It must be one of {validate_units}."
        raise ValidationError(error, status.HTTP_400_BAD_REQUEST)

    return city, state, coutnry, units
