from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import STask, STaskAdd



class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()  # Convert Pydantic model to dict
            
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()  # Ensure the task gets an ID
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            tasks_schemas = [STask.model_validate(tasks_model) for tasks_model in tasks_models]
            return tasks_schemas