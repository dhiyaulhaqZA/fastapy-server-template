from fastapi import APIRouter
from routes.example import router as example_router
from utils.responsify import Responsify

main_router = APIRouter()
main_router.include_router(example_router, prefix="/api/v1", tags=["example"])


@main_router.get("/")
async def index():
    return Responsify.success(
        { 
            "message": "Hello World" 
        }
    )