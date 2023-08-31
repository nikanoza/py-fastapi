from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool

tasks = [
    Task(id=17, title="Task 1", completed=True),
    Task(id=18, title="Buy Milk", completed=False),
    Task(id=19, title="Read book", completed=False),
    Task(id=20, title="Wash the car", completed=False),
]

@app.get("/")
def read_root():
    return {
        "info": "This is a simple todo app for managing your daily tasks",
        "tasks_list": "/tasks"
    }

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, new_task: Task):
    task_index = next((index for index, task in enumerate(tasks) if task.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_index] = new_task
    return new_task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
    return task