# pathparameter.py
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def base_get_route():
	return {"massage": "hello world!"}


@app.get('/items')
async def items_main_page():
	return {"massage": "만약 목록의 이름들을 알고 싶다면 Path Parameter에 /list를 추가하세요."}


@app.get('/items/list')
async def items_list():
	return {"items_list": fake_items_db}


@app.get('/items/{item_id}')
async def item_detail(item_id: int):
	if item_id in fake_items_detail.keys():
		return {"item_detail": fake_items_detail[item_id]}
	else:
		return {"massage": "존재하지 않는 item_id 입니다."}



fake_items_db = [{"item_id": 0}, {"item_id": 1}, {"item_id": 2}]
fake_items_detail = {0: {"item_id": 0, "item_name": "Coffee", "item_price": 2000, "item_sort": "Drink"},
                     1: {"item_id": 1, "item_name": "Water", "item_price": 950, "item_sort": "Drink"},
                     2: {"item_id": 2, "item_name": "Book", "item_price": 12000, "item_sort": "Object"}}
