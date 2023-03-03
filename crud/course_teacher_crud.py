import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import course_teacher_schema


class CourseTeacherCrud(
    BaseCrud[
        models.CourseTeacher,
        course_teacher_schema.CreateCourseTeacherSchema,
        course_teacher_schema.CreateCourseTeacherSchema,
    ]
):
    pass


crud = CourseTeacherCrud(models.CourseTeacher)
