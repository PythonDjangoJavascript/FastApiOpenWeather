
from typing import Optional


api_key: Optional[str] = None


def get_weather_api(city: str, state: Optional[str], country: Optional[str], units: str) -> dict:

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"

    url = f"api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    print(url)
