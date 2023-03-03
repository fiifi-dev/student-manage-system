from pydantic import BaseModel


class CreateCourseSchema(BaseModel):
    code: str
    name: str


class ReadCourseSchema(CreateCourseSchema):
    id: int

    class Config:
        orm_mode = True
