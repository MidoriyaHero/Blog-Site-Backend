from fastapi import APIRouter
from models.blog_model import BlogModel, UpdateBlogModel
from config.config import blogs_collection
import datetime
from data.getblog import decode_all, decodeblog
from bson import ObjectId
blog_router = APIRouter()

@blog_router.post('/blog')
def blog(items: BlogModel):
    items = dict(items)
    items['date'] = str(datetime.date.today())
    blogs_collection.insert_one(items)
    return {'message':'BLog added successfully!!!'}

@blog_router.get('/all/blog')
async def get_blogs():
    data = blogs_collection.find()
    return decode_all(data)

@blog_router.get('/blog/{id}')
async def get_blog(id: str):
    data = blogs_collection.find_one({'_id': ObjectId(id)})
    if data:
        return decodeblog(data)
    else:
        return {'message': 'Blog not found'}
    
@blog_router.put('/update/{id}')
async def update(id: str, blog: UpdateBlogModel):
    data = dict(blog.model_dump(exclude_unset=True))
    blogs_collection.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': data})

    return ({'message':'Blog updated'})

@blog_router.delete('/delete/{id}')
async def delete(id: str):
    blogs_collection.delete_one({'_id': ObjectId(id)})
    return {'message':'Blog deleted'}
