import requests
import httpx
from typing import Optional


api_key: Optional[str] = None


async def get_weather_api_async(city: str, state: Optional[str], country: Optional[str], units: str) -> dict:

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"

    # url = f"api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}"

    # Now send the async request
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # will throw an exception if status goes wrong

    data = response.json()
    forcast = data['main']  # filtering only main data

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
