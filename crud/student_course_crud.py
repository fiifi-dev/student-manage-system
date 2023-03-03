import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import student_course_schema


class StudentCourseCrud(
    BaseCrud[
        models.StudentCourse,
        student_course_schema.CreateStudentCourseSchema,
        student_course_schema.CreateStudentCourseSchema,
    ]
):
    pass


crud = StudentCourseCrud(models.StudentCourse)
