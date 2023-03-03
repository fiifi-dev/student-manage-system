import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import student_assessment_schema


class StudentAssessmentCrud(
    BaseCrud[
        models.StudentAssessment,
        student_assessment_schema.CreateStudentAssessmentSchema,
        student_assessment_schema.CreateStudentAssessmentSchema,
    ]
):
    pass


crud = StudentAssessmentCrud(models.StudentAssessment)
