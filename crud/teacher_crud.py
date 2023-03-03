import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import teacher_schema


class TeacherCrud(
    BaseCrud[
        models.Teacher,
        teacher_schema.CreateTeacherSchema,
        teacher_schema.CreateTeacherSchema,
    ]
):
    pass


crud = TeacherCrud(models.Teacher)
