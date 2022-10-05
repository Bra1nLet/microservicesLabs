from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static/"), name="static")


class Item(BaseModel):
    name: str
    price: float

    class Config:
        orm_mode = True


templates = Jinja2Templates(directory="templates")


@app.get("/create_items/", response_class=HTMLResponse)
async def create_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.post('/create_items/', response_class=HTMLResponse)
async def create_item(request: Request, item: str = Form(...), price: float = Form(...)):

    a = Item(name=item, price=price)

    inventory[len(inventory)+1] = json.loads(a.json())

    return templates.TemplateResponse("item.html", {"request": request, 'item': item})


inventory = {
    1: {
        "name": "Milk",
        "price": "32.2",
    }
}


@app.get("/", response_class=HTMLResponse)
async def all_item(request: Request):
    return templates.TemplateResponse("allitems.html", {"request": request, 'items': inventory})


@app.get("/get-item/{item_id}", response_class=HTMLResponse)
async def get_items(request: Request, item_id: int):
    return templates.TemplateResponse("allitems.html", {"request": request, 'item': inventory[item_id]})
