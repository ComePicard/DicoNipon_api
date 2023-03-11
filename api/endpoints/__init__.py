from fastapi import APIRouter
from api.version import __version__ as git_version

router = APIRouter()


@router.get("/")
def read_root():
    return {"DicoNipon": "HELLO"}
