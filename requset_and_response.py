from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator

app =FastAPI()

""" class User(BaseModel):
    name:str
    age:int """


""" @app.post("/users/")
async def create_user(user:User):
    return {"sended user" :user.name,"sendedage":user.age} """
    
""" @app.post("/users/{user_id}",response_model=User)
async def get_user(user_id:int):
    return {"name":"Silva", "age":22} """
   
   
class User(BaseModel):
    name:str
    age:int = Field(...,gt=0,le=120)
    
    @field_validator("name")
    def name_must_not_be_empty(cls,v):
        if not v:
            raise ValueError("Name must not be empty")
        return v

@app.post("/users/")
async def create_user(user:User):
    u = {"name":user.name, "age":user.age}
    return u