from fastapi import FastAPI

app = FastAPI()
@app.get("/users/")
def road_user(user_id: int,name:str):
    return {"user": user_id,"name":name}
#{"user":1,"name":John}
#http://127.0.0.1:8000/users/?user_id=1&name=john


def road_user(user_id: int,name:str=None):
    return {"user": user_id,"name":name}
#{"user":1,"name":null}
#http://127.0.0.1:8000/users/?user_id=1

