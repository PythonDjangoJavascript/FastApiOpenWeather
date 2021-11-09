from fastapi import APIRouter, responses
from starlette.templating import Jinja2Templates
from starlette.requests import Request


router = APIRouter()
templates = Jinja2Templates("templates")


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return responses.RedirectResponse(url='static/img/favicon.ico')
