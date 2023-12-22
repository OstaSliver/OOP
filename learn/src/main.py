from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson.objectid import ObjectId

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client["mydb"]
collection = db["66010840"]

class account(BaseModel):
    username: str
    password: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/post")
async def post(data: account):
    collection.insert_one(data.dict())
    return {"message": "success"}

@app.get("/get")
async def get():
    data = list(collection.find())
    serialized_data = [{"_id": str(item["_id"]), "username": item["username"], "password": item["password"]} for item in data]
    return {"message": serialized_data}