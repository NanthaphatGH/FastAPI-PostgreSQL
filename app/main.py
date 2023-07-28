import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from app.models import Book as ModelBook, Author as ModelAuthor
from app.schema import Book as SchemaBook, Author as SchemaAuthor

import os
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI()

# Configure the SQLAlchemy database connection
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# @app.get("/")
# async def root():
#     return {"message": "สวัสดีครับ คนอ่าน"}


# CRUD Operations for Book
@app.post("/book/", response_model=SchemaBook)
def create_book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.get("/book/{book_id}", response_model=SchemaBook)
def read_book(book_id: int):
    db_book = db.session.query(ModelBook).filter(ModelBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.put("/book/{book_id}", response_model=SchemaBook)
def update_book(book_id: int, book: SchemaBook):
    db_book = db.session.query(ModelBook).filter(ModelBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.rating = book.rating
    db_book.author_id = book.author_id
    db.session.commit()
    return db_book

@app.delete("/book/{book_id}", response_model=SchemaBook)
def delete_book(book_id: int):
    db_book = db.session.query(ModelBook).filter(ModelBook.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.session.delete(db_book)
    db.session.commit()
    return db_book


# CRUD Operations for Author
@app.post("/author/", response_model=SchemaAuthor)
def create_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author

@app.get("/author/{author_id}", response_model=SchemaAuthor)
def read_author(author_id: int):
    db_author = db.session.query(ModelAuthor).filter(ModelAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@app.put("/author/{author_id}", response_model=SchemaAuthor)
def update_author(author_id: int, author: SchemaAuthor):
    db_author = db.session.query(ModelAuthor).filter(ModelAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db_author.name = author.name
    db_author.age = author.age
    db.session.commit()
    return db_author

@app.delete("/author/{author_id}", response_model=SchemaAuthor)
def delete_author(author_id: int):
    db_author = db.session.query(ModelAuthor).filter(ModelAuthor.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.session.delete(db_author)
    db.session.commit()
    return db_author


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
