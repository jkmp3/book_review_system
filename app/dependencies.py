from fastapi import FastAPI

from app.routers import books, reviews

app = FastAPI()

app.include_router(books.router)
app.include_router(reviews.router)
