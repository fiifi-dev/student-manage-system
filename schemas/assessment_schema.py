from datetime import datetime
from pydantic import BaseModel


class CreateAssessmentSchema(BaseModel):
    title: str
    due_date: datetime
    total_scores: int
    posted_date: datetime = datetime.now()
    teacher_id: int
    course_id: int


class ReadAssessmentSchema(CreateAssessmentSchema):
    id: int

    class Config:
        orm_mode = True
