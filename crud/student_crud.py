import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import student_schema


class StudentCrud(
    BaseCrud[
        models.Student,
        student_schema.CreateStudentSchema,
        student_schema.CreateStudentSchema,
    ]
):
    pass


crud = StudentCrud(models.Student)
