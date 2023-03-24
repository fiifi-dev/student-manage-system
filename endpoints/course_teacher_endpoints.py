from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import dependencies
from crud import course_teacher_crud
from schemas import course_teacher_schema

router = APIRouter()


@router.post(
    "/",
    response_model=course_teacher_schema.ReadCourseTeacherSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_course_teacher(
    item: course_teacher_schema.CreateCourseTeacherSchema,
    db: Session = Depends(dependencies.get_db),
):
    return course_teacher_crud.crud.create(db, item)


@router.put(
    "/{course_teacher_id}",
    response_model=course_teacher_schema.ReadCourseTeacherSchema,
)
def update_course_teacher(
    item: course_teacher_schema.CreateCourseTeacherSchema,
    course_teacher_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return course_teacher_crud.crud.update(db, course_teacher_id, item)


@router.delete(
    "/{course_teacher_id}",
    response_model=course_teacher_schema.ReadCourseTeacherSchema,
)
def delete_course_teacher(
    course_teacher_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return course_teacher_crud.crud.destroy(db, course_teacher_id)
