import datetime
from typing import Optional, Tuple

__cache = {}
lifetime_in_hr = 1.0


def get_weather(city: str, state: Optional[str], country: str, units: str) -> Optional[dict]:
    key = __create_key(city, state, country, units)
    data: dict = __cache.get(key)

    if not data:
        return None

    last = data['time']
    time_diff = datetime.datetime.now() - last
    print(f"---------------->{time_diff}<---------")
    print(f"---------------->{key}<---------")

    # convert time diff in houre and compare
    if time_diff / datetime.timedelta(minutes=60) < lifetime_in_hr:
        return data['value']

    # now clean the cache if time limite is expired
    del __cache[key]
    return None


def set_weather(city: str, state: str, country: str, units: str, value: dict):
    key = __create_key(city, state, country, units)

    # now create the date to set latter
    data = {
        'time': datetime.datetime.now(),
        'value': value  # this value is the weather data
    }

    # now set the data to cache
    __cache[key] = data
    __clean_out_of_date()


def __create_key(city: str, state: str, country: str, units: str) -> Tuple[str, str, str, str]:
    if not city or not country or not units:
        raise Exception("City, country and units is required")

    if not state:
        state = ""

    return city.strip().lower(), state.strip().lower(), country.strip().lower(), units.strip().lower()


def __clean_out_of_date():
    for key, data in list(__cache.items()):
        time_diff = datetime.datetime.now() - data.get('time')

        if time_diff / datetime.timedelta(minutes=60) > lifetime_in_hr:
            del __cache[key]
