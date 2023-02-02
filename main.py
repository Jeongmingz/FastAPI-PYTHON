from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

# descriotion => 설명글 / deprecated => 사용여부 설정 : True(사용 불가), False(사용 가능)

@app.get('/', description="This is my first route", deprecated=True)
async def base_get_route():
	return {"massage" : "hello world!"}

@app.post("/")
async def post():
	return {"massage" : "hello form the post route"}

@app.put('/{id}')
async def put():
	return {"massage" : "hello from the put route"}

@app.get('/users')
async def list_users():
	return {"massage" : "list users route"}


# 만약 매퍼가 겹친다면 그 매퍼 중 하나를 고정시키고 싶다면
# 고정해야할 매핑을 전체 매핑 위에 배치하면 된다.
@app.get("/users/me")
async def get_current_user():
	return {'message' : 'this is the current user'}

# 파라미터에 받는 값은 자료형을 선언해 줘야한다. 그렇지 않으면 기본값은 str로 들어가게 된다.
# : int, char, str(Default), list 등
# 자료형 선언을 통해 그 자료형에 맞지 않는 값이 들어오게 되면 에러와 에러 내용을 리턴해준다.
@app.get('/users/{user_id}')
async def get_user(user_id: str):
	return {'user_id' : user_id}


class FoodEnum(str, Enum):
	fruits = "fruits"
	vegetables = "vegetables"
	dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
	if food_name == FoodEnum.vegetables:
		return {
			"food_name" : food_name,
		    "message" : "you are healthy",
		}

	if food_name.value == "fruits":
		return{
			"food_name" : food_name,
			"message" : "you are still healthy, but like sweet things",
		}

	return{
			"food_name": food_name,
			"message": "I like chocolate milk",
		}

fake_items_db = [{"item_name" : "foo"}, {"item_name" : "Bar"}, {"item_name" : "Baz"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
	return fake_items_db[skip : skip + limit]

# Dictonary.upadte => Key, Value 값 추가
@app.get("/items/{item_id}")
async def get_item(item_id:str, sample_query_param: str, q: Optional[str] = None, short: bool = False):
	item = {'item_id': item_id, 'sample_query_param': sample_query_param}
	if q:
		item.update({"q":q})
	if not short:
		item.update({"description": "asdfasdfasdfasdfasdfasdf"})
	return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
	item = {'item_id': item_id, 'owner_id': user_id}
	if q:
		item.update({"q":q})
	if not short:
		item.update({"description": "asdfasdfasdfasdfasdfasdf"})
	return item