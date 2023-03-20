from typing import Optional, List
from pydantic import BaseModel

class Film(BaseModel):
    id: Optional[str]
    title: str
    year: str
    duration: str
    country: str
    genre: str
    synopsis: str