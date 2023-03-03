from datetime import datetime
from pydantic import BaseModel


class CreateStudentCourseSchema(BaseModel):
    student_id: int
    course_id: int
    registered_date: datetime = datetime.now()


class ReadStudentCourseSchema(CreateStudentCourseSchema):
    id: int

    class Config:
        orm_mode = True
