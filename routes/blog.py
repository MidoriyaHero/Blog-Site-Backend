from fastapi import APIRouter
from models.blog_model import BlogModel
from config.config import blogs_collection
import datetime

blog_router = APIRouter()

@blog_router.post('/blog')
def blog(items: BlogModel):
    items = dict(items)
    items['date'] = str(datetime.date.today())
    blogs_collection.insert_one(items)
    return {'message':'BLog added successfully!!!'}