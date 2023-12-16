# from fastapi import FastAPI

# app = FastAPI(title='hello')


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}

# @app.get("/items/me")
# async def read_item():
#     return {"item_id": "current user"}

# @app.get("/items/{item_id}")
# async def read_item(item_id:str):
#     return {"item_id": item_id}

# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI(title='hello')

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
