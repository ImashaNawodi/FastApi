from fastapi import FastAPI

app = FastAPI()

# Path Parameters in FastAPI:
# - Path parameters capture values from the URL and pass them as function arguments.
# - Define them inside curly braces `{}` in the route.
# - FastAPI automatically converts types based on type hints.
# - Example: Accessing `/users/5` returns `{"user": 5}`, and `/items/laptop` returns `{"item": "laptop"}`.

@app.get("/users/{user_id}")
def road_user(user_id: int):
    return {"user": user_id}

@app.get("/items/{item_name}")
def new_item(item_name: str):
    return {"item": item_name}
