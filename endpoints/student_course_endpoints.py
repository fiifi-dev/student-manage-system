import sqlalchemy as sa
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import dependencies, models
from crud import student_course_crud
from schemas import student_course_schema, course_schema

router = APIRouter()


@router.post(
    "/",
    response_model=student_course_schema.ReadStudentCourseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_student_course(
    item: student_course_schema.CreateStudentCourseSchema,
    db: Session = Depends(dependencies.get_db),
):
    return student_course_crud.crud.create(db, item)


@router.put(
    "/{student_course_id}",
    response_model=student_course_schema.ReadStudentCourseSchema,
)
def update_student_course(
    item: student_course_schema.CreateStudentCourseSchema,
    student_course_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return student_course_crud.crud.update(db, student_course_id, item)


@router.delete(
    "/{student_course_id}",
    response_model=student_course_schema.ReadStudentCourseSchema,
)
def delete_student_course(
    student_course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return student_course_crud.crud.destroy(db, student_course_id)
