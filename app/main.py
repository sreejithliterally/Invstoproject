from fastapi import FastAPI
import models
from database import engine
from routers import csv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)

app.include_router(csv.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}