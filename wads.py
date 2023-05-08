from fastapi import FastAPI, Path
from typing import Optional

from pydantic import BaseModel

app=FastAPI()


class Todo(BaseModel):
    name:str

#Todo data with id 1
Todos ={
    1:Todo(name="buy groceries"),
    
    2:Todo(name="walk the plank")
}

#setting endpoint
@app.get("/")
def index():
    return{"Data":"Hello World"}

@app.get("/get-Todo/{id}")

def get_Todo(id: int= Path(description="The Id of the Todo you want to see")):
    return Todos[id]


@app.get("/get-Todo-by-name")

def get_Todo(*, name:Optional[str]="None" ,test: str):
    for Todo_id in Todos:
        if Todos[Todo_id]["name"]==name:
            return Todos[Todo_id]
    return {"error":"Todo does not exist"}


@app.get("/get-Todo-by-name{Todo_id}")
def get_Todo(*,Todo_id:int, name:Optional[str]="None" ,test: str):
    for Todo_id in Todos:
        if Todos[Todo_id]["name"]==name:
            return Todos[Todo_id]
    return {"error":"Todo does not exist"}


#POST method


@app.post("/create-Todo/{Todo_id}")
def create_Todo(Todo_id:int, Todo:Todo):
    if Todo_id in Todos:
        return {"error":"Todo ID already EXIST"}
    Todos[Todo_id]=Todo
    return Todos[Todo_id]

class UpdateTodo(BaseModel):
    name:Optional[str] = None

@app.put("/update-Todo/{Todo_id}")
def update_Todo(Todo_id:int, Todo:UpdateTodo):
    if Todo_id not in Todos:
        return {"error": "Todo ID does not EXIST"}
    
    if Todo.name != None:
         Todos[Todo_id].name=Todo.name
    return Todos[Todo_id]

#delete method
@app.delete("/delete-Todo/{Todo_id}")
def delete_Todo(Todo_id:int):
    if Todo_id not in Todos:
        return {"error": "Todo ID does not EXIST"}
    
    del Todos[Todo_id]
    return {"data":"delete successful"}
