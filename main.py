import os
from fastapi import FastAPI
from routes import main_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:3000/"
]

app = FastAPI()
app.include_router(main_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)