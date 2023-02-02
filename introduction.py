# introduction.py
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def base_get_route():
	return {"massage" : "hello world!"}