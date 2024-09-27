from pydantic import BaseModel



class ToDoCreate(BaseModel):
    title: str
    is_done: bool = False
    starred: bool = False

    class Config:
        allow_population_by_field_name = True

class ToDoResponse(ToDoCreate):
    id: int
    is_done: bool = False
    starred: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            'is_done': 'isDone',
            'starred': 'Starred'
        }