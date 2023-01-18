import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import blogs_r
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(blogs_r.router)
