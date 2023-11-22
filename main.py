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

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id:str):
#     return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# app = FastAPI()
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 }
#             ]
#         }
#     }

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):
#     name: str = Field(examples=["Foo"])
#     description: str | None = Field(default=None, examples=["A very nice Item"])
#     price: float = Field(examples=[35.4])
#     tax: float | None = Field(default=None, examples=[3.2])

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# examples in JSON Schema - OpenAPI¶
# When using any of:

# Path()
# Query()
# Header()
# Cookie()
# Body()
# Form()
# File()
# you can also declare a group of examples with additional information that will be added to their JSON Schemas inside of OpenAPI.

# from typing import Annotated
# from fastapi import FastAPI, Query

# app = FastAPI()
# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# This specific regular expression pattern checks that the received parameter value:
# ^: starts with the following characters, doesn't have characters before.
# fixedquery: has the exact value fixedquery.
# $: ends there, doesn't have any more characters after fixedquery

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items

# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()
# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(title="Query string", min_length=3)] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             pattern="^fixedquery$",
#             deprecated=True,
#             include_in_schema=False
#         )

# from typing import Annotated

# from fastapi import FastAPI, Path

# app = FastAPI()
# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import Annotated

# from fastapi import FastAPI, Path, Query

# app = FastAPI()
# @app.get("/items/{item_id}")
# async def read_items(
#     *,
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results

# Body(embed=True)

# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Image(BaseModel):
#     url: str
#     name: str

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     image: Image | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()
# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# @app.post("/images/multiple/")
# async def create_multiple_images(images: list[Image]):
#     return images

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item = Body(
#         examples=[
#             {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             },
#             {
#                 "name": "Bar",
#                 "price": "35.4",
#             },
#             {
#                 "name": "Baz",
#                 "price": "thirty five point four",
#             },
#         ],
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# Using the openapi_examples Parameter¶
# You can declare the OpenAPI-specific examples in FastAPI with the parameter openapi_examples for:

# Path()
# Query()
# Header()
# Cookie()
# Body()
# Form()
# File()
# The keys of the dict identify each example, and each value is another dict.

# Each specific example dict in the examples can contain:

# summary: Short description for the example.
# description: A long description that can contain Markdown text.
# value: This is the actual example shown, e.g. a dict.
# externalValue: alternative to value, a URL pointing to the example. Although this might not be supported by as many tools as value.

# from typing import Annotated
# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Annotated[
#         Item,
#         Body(
#             openapi_examples={
#                 "normal": {
#                     "summary": "A normal example",
#                     "description": "A **normal** item works correctly.",
#                     "value": {
#                         "name": "Foo",
#                         "description": "A very nice Item",
#                         "price": 35.4,
#                         "tax": 3.2,
#                     },
#                 },
#                 "converted": {
#                     "summary": "An example with converted data",
#                     "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#                     "value": {
#                         "name": "Bar",
#                         "price": "35.4",
#                     },
#                 },
#                 "invalid": {
#                     "summary": "Invalid data is rejected with an error",
#                     "value": {
#                         "name": "Baz",
#                         "price": "thirty five point four",
#                     },
#                 },
#             },
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results

# Other data types¶
# Here are some of the additional data types you can use:

# UUID:
# A standard "Universally Unique Identifier", common as an ID in many databases and systems.
# In requests and responses will be represented as a str.
# datetime.datetime:
# A Python datetime.datetime.
# In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15T15:53:00+05:00.
# datetime.date:
# Python datetime.date.
# In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15.
# datetime.time:
# A Python datetime.time.
# In requests and responses will be represented as a str in ISO 8601 format, like: 14:23:55.003.
# datetime.timedelta:
# A Python datetime.timedelta.
# In requests and responses will be represented as a float of total seconds.
# Pydantic also allows representing it as a "ISO 8601 time diff encoding", see the docs for more info.
# frozenset:
# In requests and responses, treated the same as a set:
# In requests, a list will be read, eliminating duplicates and converting it to a set.
# In responses, the set will be converted to a list.
# The generated schema will specify that the set values are unique (using JSON Schema's uniqueItems).
# bytes:
# Standard Python bytes.
# In requests and responses will be treated as str.
# The generated schema will specify that it's a str with binary "format".
# Decimal:
# Standard Python Decimal.
# In requests and responses, handled the same as a float.

# from datetime import datetime, time, timedelta
# from typing import Annotated
# from uuid import UUID
# from fastapi import Body, FastAPI

# app = FastAPI()
# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: Annotated[datetime | None, Body()] = None,
#     end_datetime: Annotated[datetime | None, Body()] = None,
#     repeat_at: Annotated[time | None, Body()] = None,
#     process_after: Annotated[timedelta | None, Body()] = None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }

# from typing import Annotated
# from fastapi import FastAPI, Header

# app = FastAPI()
# @app.get("/items/")
# async def read_items(
#     strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
# ):
#     return {"strange_header": strange_header}

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()
# class Item(BaseModel):
#     name: str = Field(examples=["Foo"])
#     description: str | None = Field(default=None, examples=["A very nice Item"])
#     price: float = Field(examples=[35.4])
#     tax: float | None = Field(default=None, examples=[3.2])

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results





