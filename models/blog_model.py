from pydantic import BaseModel

class BlogModel(BaseModel):
    title: str
    content: str
    author: str
    tags: list[str]
    date: str

class UpdateBlogModel(BaseModel):
    title: str = None
    content: str = None
    author: str = None
    tags: list[str] = None
    date: str = None