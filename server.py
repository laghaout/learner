# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:40:46 2024
"""

from fastapi import FastAPI, HTTPException
import learner.utilities as util
import learner.wrangler as wra
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def root(task: str = None):
    # http://127.0.0.1:8000/?task=task
    from main import main
    output = main(task)
    output = util.df_to_pydantic(
        output.report.serve['prediction'].reset_index(),
        wra.Output
        )    
    return output


#%% Server

if True:

    # Use this for the data from the wranglers or for the inferences from the 
    # serving.
    class Item(BaseModel):
        city: str = None
        age: int = None
    items = {'Joe': Item(city='Charlottetown', age=42), 'Jane': Item(city='Toronto', age=36)}

    @app.get("/index")
    def index() -> dict[str, dict[str, Item]]:
        return {'items': items}

    @app.get("/index/{item_id}")
    def index_id(item_id: str) -> Item:
        if item_id not in items:
            raise HTTPException(status_code=404, detail=f"{item_id=} does not exist")
        return items[item_id]
    
    # Example of basic function: Year of birth
    @app.get("/yob")
    def yob(age: int, current_year: int = 2025) -> int:
        # http://127.0.0.1:8000/yob/?age=38&current_year=1981
        return current_year - age
        
    @app.get("/convert")
    def convert(Fahrenheit: float) -> float:
        return (Fahrenheit - 32)*5/9

#%% Client for inference (once a model has been trained and deployed).

if False:
    import json
    import requests
    
    data = [{"age": 100, "city": "Toronto"},
            {"age": 42, "city": "Rabat"},
            {"age": 12, "city": "Amizmiz"}]
    
    url = 'http://localhost:8000/predict/'
    
    predictions = []
    for record in data:
        payload = {'features': record}
        payload = json.dumps(record)
        response = requests.post(url, data=payload)
        predictions.append(response.json()['prediction'])
    
    print(predictions)    