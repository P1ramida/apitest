from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
import uvicorn
from utils import load_storage, save_storage, generate_short_url
import os
import json
app = FastAPI()


@app.get("/",summary="Main",tags=['Main'])
async def hello():
    return {"message": "Hi, and welcome, please check /docs"}

@app.post("/",summary="genrate url",tags=['GenerateUrl'],status_code=201)
async def generate_url():
    new_short_url = generate_short_url()
    save_storage(new_short_url)
    return {"short_url":f"{new_short_url}"}

@app.get("/{short_url}",summary="get_current_url",tags=['CurrentUrl'],status_code=307)
async def get_current_url(short_url:str):
    
    with open(load_storage(),'r') as f:
        data = json.load(f)

    current_url = data.get(short_url) 
    if current_url:
        return RedirectResponse(url=current_url, status_code=307)
    raise HTTPException(status_code=404,detail="Short url is not exsist")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)