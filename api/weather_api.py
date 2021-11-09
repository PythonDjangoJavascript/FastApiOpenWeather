from fastapi.routing import APIRouter


router = APIRouter()


@router.get('/api/weather')
def weather():
    return "weatehr report"
