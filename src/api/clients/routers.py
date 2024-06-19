from fastapi import APIRouter

router = APIRouter(prefix='/clients')


@router.post(path='')
def create_client():
    ...