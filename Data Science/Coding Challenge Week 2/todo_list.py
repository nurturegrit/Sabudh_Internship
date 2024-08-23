from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    title: str | None = None


TODO = [{
        "id":2,
        "title": "Buy Groceries"
      }]


@app.get("/todo")
def get_todo_items(name, age:int):
    return TODO


@app.post('/new-todo')
def new_todo(todo_item:Item):
    TODO.append(todo_item)
    return todo_item


@app.get("/another/{name}/")
# try without = None
def greet(name, age:int, gender:str | None = None, marks:int = 100):
    return {"Response": f"Hello {name}!, you are a {age} years old {gender} with {marks} Marks"}
import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)
