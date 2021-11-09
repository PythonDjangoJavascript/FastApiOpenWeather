import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from pathlib import Path
import json

from api import weather_api
from views import home
from services import open_weather_service


api = FastAPI()


def configure():
    """Configure the app"""
    # api_key, database etc
    config_routing()
    config_api_key()


def config_routing():
    """Configure routing of this app"""
    api.mount('/static/', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


def config_api_key():
    """Configure OpenWeatherAPIKey"""
    file = Path('settings.json').absolute()

    if not file.exists():
        print(
            f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise Exception(
            "settings.json file not found, you cannot continue, please see settings_template.json")

    with open('settings.json') as settings_file:
        settings = json.load(settings_file)
        open_weather_service.api_key = settings.get('api_key')
        print(settings.get('api_key'))


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
