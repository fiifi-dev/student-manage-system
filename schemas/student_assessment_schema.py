from datetime import datetime
from pydantic import BaseModel


class CreateStudentAssessmentSchema(BaseModel):
    assessment_id: int
    student_id: int
    submission_date: datetime = datetime.now()


class ReadStudentAssessmentSchema(CreateStudentAssessmentSchema):
    id: int
    score: float

    class Config:
        orm_mode = True
