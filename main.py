from typing import Optional, Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as task_router
from schemas import STaskAdd, STask

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Creating tables...")
    await create_tables()
    print("Tables created.")
    yield
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.include_router(task_router)


# @app.get("/tasks")
# def get_tasks():
#     task = (Task(name='Задача 1', description='Описание задачи 1'))
#     return {"tasks": task}


