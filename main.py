from fastapi import FastAPI
from app.hash_table import HashTable

hash_table = HashTable()
app = FastAPI()

@app.get("/")
async def root():
    return {"Greetings": "Welcome to FastAPI!"}

@app.post("/add")
async def add_entry(key: str, value):
    hash_table.add(key, value)
    return f"Key-value pair {key}-{value} added"

@app.delete("/delete")
async def delete_entry(key: str):
    hash_table.delete(key)
    return f"Key: {key}deleted"

@app.get("/get")
async def get_value(key: str):
    return hash_table.get(key)
