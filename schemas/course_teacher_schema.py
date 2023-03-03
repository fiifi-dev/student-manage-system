from datetime import datetime
from pydantic import BaseModel


class CreateCourseTeacherSchema(BaseModel):
    course_id: int
    teacher_id: int
    registered_date: datetime = datetime.now()


class ReadCourseTeacherSchema(CreateCourseTeacherSchema):
    id: int

    class Config:
        orm_mode = True
