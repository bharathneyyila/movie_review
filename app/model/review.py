from pydantic import BaseModel

class Review(BaseModel):
    reviewer: str
    rating: float
    comment: str
  
