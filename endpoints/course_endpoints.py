import sqlalchemy as sa
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import dependencies, models
from crud import course_crud
from helpers import general_schemas
from schemas import course_schema, teacher_schema

router = APIRouter()


@router.get(
    "/",
    response_model=general_schemas.ListBaseSchema[course_schema.ReadCourseSchema],
)
def list_courses(
    db: Session = Depends(dependencies.get_db),
    paginate_params: dict = Depends(dependencies.paginate_params),
):
    return course_crud.crud.read_list(
        db,
        skip=paginate_params["skip"],
        limit=paginate_params["limit"],
    )


@router.post(
    "/",
    response_model=course_schema.ReadCourseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_course(
    item: course_schema.CreateCourseSchema, db: Session = Depends(dependencies.get_db)
):
    return course_crud.crud.create(db, item)


@router.get(
    "/{course_id}",
    response_model=course_schema.ReadCourseSchema,
)
def get_course(
    course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return course_crud.crud.read_one(db, course_id)


@router.get(
    "/{course_id}/teachers",
    response_model=list[teacher_schema.ReadTeacherSchema],
)
def get_teachers(
    course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    stmt = sa.select(models.Course).where(models.Course.id == course_id)
    course = db.scalar(stmt)

    if course is None:
        return []

    return course.assessments


@router.put(
    "/{course_id}",
    response_model=course_schema.ReadCourseSchema,
)
def update_course(
    item: course_schema.CreateCourseSchema,
    course_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return course_crud.crud.update(db, course_id, item)


@router.delete(
    "/{course_id}",
    response_model=course_schema.ReadCourseSchema,
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_course(
    course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return course_crud.crud.destroy(db, course_id)


@router.get(
    "/{course_id}/students",
    response_model=list[course_schema.ReadCourseSchema],
)
def get_students(
    course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    stmt = sa.select(models.Course).where(models.Course.id == course_id)
    course = db.scalar(stmt)

    if course is None:
        return []

    return course.students


@router.get("/{course_id}/generate_assessment_file")
def download_assessment_file(
    course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return {"detail": "todo"}
