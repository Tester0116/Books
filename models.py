
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Integer, Column, String
from database import Base


# Модель для книги

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)


# Класс для входных данных POST-запроса
class BookCreate(BaseModel):
    title: str
    author: str
    year: int

# Класс для входных данных PUT-запроса


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
