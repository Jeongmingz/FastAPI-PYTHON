from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.get("/")
async def api_home() -> dict:
	return {'msg': 'CEMS Fast-API Main Page'}


@app.get("/user")
async def get_user_list() -> dict:
	pass


@app.get("/login")
async def user_login() -> int:
	# login_check = 1 : 성공
	# login_check = 0 : 실패 (실패 이유에 대해 설명해야 함. 비밀번호 오류, 존재하지 않는 계정 등)
	login_check = 0

	return login_check


@app.put("/signup")
async def user_signup():
	pass


@app.put("/find")
async def user_find(action: List):
	pass
