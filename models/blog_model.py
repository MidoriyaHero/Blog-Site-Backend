from pydantic import BaseModel

class BlogModel(BaseModel):
    title: str
    content: str
    author: str
    tags: list[str]
    date: str