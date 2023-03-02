from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# descriotion => 설명글 / deprecated => 사용여부 설정 : True(사용 불가), False(사용 가능)
#
# @app.get('/', description="This is my first route", deprecated=True)
# async def base_get_route():
# 	return {"massage": "hello world!"}
#
#
# @app.post("/")
# async def post():
# 	return {"massage": "hello form the post route"}
#
#
# @app.put('/{id}')
# async def put():
# 	return {"massage": "hello from the put route"}
#
#
# @app.get('/users')
# async def list_users():
# 	return {"massage": "list users route"}
#
#
# # 만약 매퍼가 겹친다면 그 매퍼 중 하나를 고정시키고 싶다면
# # 고정해야할 매핑을 전체 매핑 위에 배치하면 된다.
# @app.get("/users/me")
# async def get_current_user():
# 	return {'message': 'this is the current user'}
#
#
# # 파라미터에 받는 값은 자료형을 선언해 줘야한다. 그렇지 않으면 기본값은 str로 들어가게 된다.
# # : int, char, str(Default), list 등
# # 자료형 선언을 통해 그 자료형에 맞지 않는 값이 들어오게 되면 에러와 에러 내용을 리턴해준다.
# @app.get('/users/{user_id}')
# async def get_user(user_id: str):
# 	return {'user_id': user_id}
#
#
# class FoodEnum(str, Enum):
# 	fruits = "fruits"
# 	vegetables = "vegetables"
# 	dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
# 	if food_name == FoodEnum.vegetables:
# 		return {
# 			"food_name": food_name,
# 			"message": "you are healthy",
# 			}
#
# 	if food_name.value == "fruits":
# 		return {
# 			"food_name": food_name,
# 			"message": "you are still healthy, but like sweet things",
# 			}
#
# 	return {
# 		"food_name": food_name,
# 		"message": "I like chocolate milk",
# 		}
#
#
# fake_items_db = [{"item_name": "foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# # Dictonary.upadte => Key, Value 값 추가
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, sample_query_param: str, q: Optional[str] = None, short: bool = False):
# 	item = {'item_id': item_id, 'sample_query_param': sample_query_param}
# 	if q:
# 		item.update({"q": q})
# 	if not short:
# 		item.update({"description": "asdfasdfasdfasdfasdfasdf"})
# 	return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
# 	item = {'item_id': item_id, 'owner_id': user_id}
# 	if q:
# 		item.update({"q": q})
# 	if not short:
# 		item.update({"description": "asdfasdfasdfasdfasdfasdf"})
# 	return item
#
#
# class Item(BaseModel):
# 	name: str
# 	description: Optional[str] = None
# 	price: float
# 	tax: Optional[float] = None
#
#
# @app.post('/items')
# async def create_item(item: Item):
# 	item_dict = item.dict()
# 	# 현재 item 은 Item class 이기 때문에 .을 사용해 변수에 접근 할 수 있다.
# 	# 만약 dictionary 형태라면, dict.get('Keyname') | dict['Keyname'] 을 통해 접근해야 한다.
# 	if item.tax:
# 		price_with_tex = item.price + item.tax
# 		item_dict.update({"price_with_tax": price_with_tex})
# 	return item_dict
#
#
# @app.put('/items/{item_id}')
# async def create_item_with_put(item_id: int, item: Item, q: Optional[str]):
# 	result = {'item_id': item_id, **item.dict()}
# 	if q:
# 		result.update({'q': q})
# 	return result
#
#
# @app.get('/items')
# async def read_items(q: Optional[list[str]] = Query("fiexdquery", min_length=3, max_length=10)):
# 	results = {'items': [{"item_id": "Foo"}, {'item_id': 'Bar'}]}
# 	if q:
# 		results.update({'q': q})
# 	return results
#
#
# @app.get('/items_hidden')
# async def hidden_query_route(hidden_query: Optional[str] = Query(None, include_in_schema=False)):
# 	if hidden_query:
# 		return {'hidden_query': hidden_query}
# 	return {'hidden_query': "Not Found"}
#
#
# @app.get('/items_validation/{item_id}')
# async def read_items_validation(item_id: int = Path(..., title='The ID of the item to get'), q: Optional[str] = Query(None, alias='item query')):
# 	results = {"item_id": item_id}
# 	if q:
# 		results.update({'q': q})
# 	return results


"""
Part 7: Body - Multiple Parameter
"""


class Item(BaseModel):
	name: str
	description: Optional[str]
	price: float
	tax: Optional[float]


class User(BaseModel):
	username: str
	full_name: Optional[str]


class Importance(BaseModel):
	importance: int


@app.get('/items/{item_id}')
async def update_item(
		*,
		item_id: int = Path(..., title='The ID of the item to get', ge=0, le=100),
		q: Optional[str] = Query(None),
		item: Optional[Item],
		user: User,
		importance: Importance = Body(...)
		):
	results = {'item_id': item_id}
	if q:
		results.update({'q': q})
	if item:
		results.update({'results': results})
	if user:
		results.update({'user': user})
	if importance:
		results.update({'importance': importance})
	return results
