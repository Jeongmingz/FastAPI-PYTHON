from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.get("/user")
async def get_user_list() -> dict:
	pass


@app.get("/login")
async def user_login() -> int:
	pass


@app.put("/signup")
async def user_signup():
	pass


@app.put("/find")
async def user_find(action: List):
	pass
