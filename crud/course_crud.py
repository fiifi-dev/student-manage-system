import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import course_schema


class CourseCrud(
    BaseCrud[
        models.Course,
        course_schema.CreateCourseSchema,
        course_schema.CreateCourseSchema,
    ]
):
    pass


crud = CourseCrud(models.Course)
