from fastapi import FastAPI
from app.hash_table import HashTable

hash_table = HashTable()
app = FastAPI()

@app.get("/")
async def root():
    return {"Greetings": "Welcome to FastAPI!"}