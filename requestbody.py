# requestbody.py
from fastapi import FastAPI
from pydantic import BaseModel

# Optional : Optional 을 선언한 변수는 None값이 들어올 수 있다. 즉, 선택가능하다.
from typing import Optional


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


@app.get('/items/detail_list')
async def item_detail_list(find: str = 'all'):
	if find == 'all':
		return fake_items_detail_list
	else:
		return [item for item in fake_items_detail_list if item['item_sort'] == find]


@app.get('/items/{item_id}')
async def item_detail(item_id: int):
	if item_id in fake_items_detail.keys():
		return {"item_detail": fake_items_detail[item_id]}
	else:
		return {"massage": "존재하지 않는 item_id 입니다."}


class Item(BaseModel):
	item_id: int
	item_name: str
	item_price: int
	item_sort: Optional[str] = "Object"


@app.post('/items')
async def create_item(item: Item):
	item_dict = item.dict()
	# Dictionary.update() => 해당 Dictionary에 값을 수정, 추가하는 function이다.
	item_dict.update({"item_sort": item.item_name.split('_')[-1]})

	return item_dict

fake_items_db = [{"item_id": 0}, {"item_id": 1}, {"item_id": 2}]

fake_items_detail = {0: {"item_id": 0, "item_name": "Coffee", "item_price": 2000, "item_sort": "Drink"},
                     1: {"item_id": 1, "item_name": "Water", "item_price": 950, "item_sort": "Drink"},
                     2: {"item_id": 2, "item_name": "Book", "item_price": 12000, "item_sort": "Object"}}

fake_items_detail_list = list(fake_items_detail.values())
