
from fastapi import FastAPI, HTTPException

from database import SessionLocal
from models import Book, BookCreate, BookUpdate


app = FastAPI(
    title="Book Store"
)


# Получение списка всех книг
@app.get("/books")
def get_books():
    db = SessionLocal()
    books = db.query(Book).all()
    return books


# Добавление новой книги
@app.post("/books")
def create_book(book: BookCreate):
    db = SessionLocal()
    new_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# Получение информации о книге по ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# Обновление информации о книге по ID
@app.put("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    db = SessionLocal()
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_update.title:
        book.title = book_update.title
    if book_update.author:
        book.author = book_update.author
    if book_update.year:
        book.year = book_update.year

    db.commit()
    db.refresh(book)
    return book


# Удаление книги по ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}


# Пагинация книг (Нужно доработать)
# @app.get("/books/pagination")
# def get_books_pag(page: int = 1, limit: int = 10):
#     db = SessionLocal()
#     start_index = (page - 1) * limit
#     end_index = start_index + limit
#     books = db.query(Book).offset(start_index).limit(limit).all()
#     return books[:end_index]
