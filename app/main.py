from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Member(BaseModel):
    name: str
    height:float
    is_adult:Union[bool, None] = None

@app.get("/")
def read_root():
    return {"AMA is here" : "Sunday"}

@app.get("/members/{member_id}")
def read_names(member_id:int, q:Union[str, None]=None):
    return{"member_id":member_id,"q":q}


@app.put("/members/{member_id}")
def update_member(member_id:int,member:Member):
    return {"member_name":member.name, "member_id":member_id}
