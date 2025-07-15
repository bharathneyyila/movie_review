from fastapi import FastAPI
from app.model.movie import Movie
from app.model.review import Review
from app.utils.file_handler import save_data, load_data
from app.utils.helpers import calculate_average_rating
import logging

app = FastAPI()

logging.basicConfig(
    filename="app/log/app.log", 
    level=logging.INFO, 
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

DATA_FILE = "app/json/data.json"

@app.post("/add_review/")
def add_review(movie: Movie):
    data = load_data(DATA_FILE)

    existing = next((m for m in data if m["title"].lower() == movie.title.lower()), None)
    if existing:
        existing["reviews"].extend(movie.reviews)
    else:
        data.append(movie.dict())

    save_data(DATA_FILE, data)
    logging.info(f"Review added for movie: {movie.title}")
    return {"message": "Review added"}

@app.get("/average_rating/{title}")
def average_rating(title: str):
    data = load_data(DATA_FILE)
    movie = next((m for m in data if m["title"].lower() == title.lower()), None)

    if not movie:
        return {"error": "Movie not found"}

    avg = calculate_average_rating(movie["reviews"])
    return {"title": title, "average_rating": avg}
