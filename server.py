# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:40:46 2024

@author: amine

Launch with uvicorn server:app --reload
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str = None
    age: int = None

items = {0: Item(name='Amine', age=42), 1: Item(name='Joe', age=72)}

def yob(age: int, current_year: int) -> int:
    return current_year - age

@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {'items': items}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"{item_id=} does not exist")
    return items[item_id]
    
@app.post("/predict")
def predict(data:dict):
    return {'prediction': data['age']*7.4}


@app.get("/predict2")
def predict2(age:int):
    return age*7.4

@app.get("/yob/")
def get_yob(age: int, current_year: Optional[int] = None):
    if current_year is None:
        from datetime import datetime
        current_year = datetime.now().year
    year_of_birth = yob(age, current_year)
    return {"age": age, "current_year": current_year, "year_of_birth": year_of_birth}

# http://127.0.0.1:8000/yob/?age=38&current_year=1981

#%%

