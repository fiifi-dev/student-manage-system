import sqlalchemy as sa
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import models, dependencies
from crud import student_crud
from helpers import general_schemas
from schemas import student_schema, course_schema, assessment_schema

router = APIRouter()


@router.get(
    "/",
    response_model=general_schemas.ListBaseSchema[student_schema.ReadStudentSchema],
)
def list_students(
    db: Session = Depends(dependencies.get_db),
    paginate_params: dict = Depends(dependencies.paginate_params),
):
    return student_crud.crud.read_list(
        db,
        skip=paginate_params["skip"],
        limit=paginate_params["limit"],
    )


@router.post(
    "/",
    response_model=student_schema.ReadStudentSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    item: student_schema.CreateStudentSchema, db: Session = Depends(dependencies.get_db)
):
    return student_crud.crud.create(db, item)


@router.get(
    "/{student_id}",
    response_model=student_schema.ReadStudentSchema,
)
def get_student(
    student_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return student_crud.crud.read_one(db, student_id)


@router.put(
    "/{student_id}",
    response_model=student_schema.ReadStudentSchema,
)
def update_student(
    item: student_schema.CreateStudentSchema,
    student_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return student_crud.crud.update(db, student_id, item)


@router.delete(
    "/{student_id}",
    response_model=student_schema.ReadStudentSchema,
)
def delete_student(
    student_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return student_crud.crud.destroy(db, student_id)


@router.get(
    "/{student_id}/courses",
    response_model=list[course_schema.ReadCourseSchema],
)
def get_courses(
    student_id: int,
    db: Session = Depends(dependencies.get_db),
):
    stmt = sa.select(models.Student).where(models.Student.id == student_id)
    student = db.scalar(stmt)

    if student is None:
        return []

    return student.courses


@router.get(
    "/{student_id}/assessments",
    response_model=list[assessment_schema.ReadAssessmentSchema],
)
def get_assessments(
    student_id: int,
    db: Session = Depends(dependencies.get_db),
):
    stmt = sa.select(models.Student).where(models.Student.id == student_id)
    student = db.scalar(stmt)

    if student is None:
        return []

    return student.assessments
