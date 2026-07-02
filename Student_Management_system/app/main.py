from fastapi import FastAPI
from app.routes import student

app=FastAPI()

app.include_router(student.router)