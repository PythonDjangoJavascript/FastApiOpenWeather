import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home


api = FastAPI()


def configure():
    """Configure the app"""
    # api_key, database etc
    config_routing()


def config_routing():
    """Configure routing of this app"""
    api.mount('/static/', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
