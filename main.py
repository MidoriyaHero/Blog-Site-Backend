from fastapi import FastAPI
from routes.endpoint import endpoint 
from routes.blog import blog_router

app = FastAPI() 
app.include_router(endpoint)
app.include_router(blog_router)