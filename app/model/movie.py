from pydantic import BaseModel
from typing import List
from .review import Review

class Movie(BaseModel):
    title: str
    reviews: List[Review]
