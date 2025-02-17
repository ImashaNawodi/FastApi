from fastapi import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/users/1/details?include_email=false

@app.get("/users/{user_id}/details")
def road_user_details(user_id: int,include_email:bool=False):
    if include_email:
        return {"user_id" :user_id, "include_email": "email included"}
    
    else:
        return {"user_id" :user_id, "include_email": "email is not included",}