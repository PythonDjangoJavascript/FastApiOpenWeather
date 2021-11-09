import uvicorn
from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.requests import Request


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static/', StaticFiles(directory='static'), name='static')


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')
