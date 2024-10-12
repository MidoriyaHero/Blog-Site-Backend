from fastapi import APIRouter

endpoint = APIRouter()

@endpoint.get("/")
async def test_endpoint():
    return {'message':'API works successfully!!!'}