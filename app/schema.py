from pydantic import BaseModel

class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        # orm_mode = True   # Comment out or remove the old 'orm_mode'
        from_attributes = True  # Use the new 'from_attributes' for Pydantic v2.x

class Author(BaseModel):
    name: str
    age: int

    class Config:
        # orm_mode = True   # Comment out or remove the old 'orm_mode'
        from_attributes = True  # Use the new 'from_attributes' for Pydantic v2.x
