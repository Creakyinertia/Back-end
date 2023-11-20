# from fastapi import BackgroundTasks, FastAPI

# app = FastAPI()


# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)


# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}

# from fastapi import FastAPI

# description = """
# ChimichangApp API helps you do awesome stuff. 🚀

# ## Items

# You can **read items**.

# ## Users

# You will be able to:

# * **Create users** (_not implemented_).
# * **Read users** (_not implemented_).
# """

# app = FastAPI(
#     title="ChimichangApp",
#     description=description,
#     summary="Deadpool's favorite app. Nuff said.",
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact={
#         "name": "Deadpoolio the Amazing",
#         "url": "http://x-force.example.com/contact/",
#         "email": "dp@x-force.example.com",
#     },
#     license_info={
#         "name": "Apache 2.0",
#         # "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
#         "identifier": "MIT",
#     },
# )


# @app.get("/items/")
# async def read_items():
#     return [{"name": "Katana"}]


# from fastapi import FastAPI

# tags_metadata = [
#     {
#         "name": "users",
#         "description": "Operations with users. The **login** logic is also here.",
#     },
#     {
#         "name": "items",
#         "description": "Manage items. So _fancy_ they have their own docs.",
#         "externalDocs": {
#             "description": "Items external docs",
#             "url": "https://fastapi.tiangolo.com/",
#         },
#     },
# ]

# app = FastAPI(openapi_tags=tags_metadata)


# @app.get("/users/", tags=["users"])
# async def get_users():
#     return [{"name": "Harry"}, {"name": "Ron"}]


# @app.get("/items/", tags=["items"])
# async def get_items():
#     return [{"name": "wand"}, {"name": "flying broom"}]
# from fastapi import FastAPI
# from fastapi.testclient import TestClient

# app = FastAPI()

# @app.get("/")
# async def read_main():
#     return {"msg": "Hello World"}

# client = TestClient(app)

# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}
