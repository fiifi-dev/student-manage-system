import sqlalchemy as sa
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import dependencies, models
from crud import teacher_crud
from helpers import general_schemas
from schemas import teacher_schema

router = APIRouter()


@router.get(
    "/",
    response_model=general_schemas.ListBaseSchema[teacher_schema.ReadTeacherSchema],
)
def list_teacher(
    db: Session = Depends(dependencies.get_db),
    paginate_params: dict = Depends(dependencies.paginate_params),
):
    return teacher_crud.crud.read_list(
        db,
        skip=paginate_params["skip"],
        limit=paginate_params["limit"],
    )


@router.post(
    "/",
    response_model=teacher_schema.ReadTeacherSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_teacher(
    item: teacher_schema.CreateTeacherSchema, db: Session = Depends(dependencies.get_db)
):
    return teacher_crud.crud.create(db, item)


@router.get(
    "/{teacher_id}",
    response_model=teacher_schema.ReadTeacherSchema,
)
def get_teacher(
    teacher_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return teacher_crud.crud.read_one(db, teacher_id)


@router.put(
    "/{teacher_id}",
    response_model=teacher_schema.ReadTeacherSchema,
)
def update_teacher(
    item: teacher_schema.CreateTeacherSchema,
    teacher_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return teacher_crud.crud.update(db, teacher_id, item)


@router.delete(
    "/{teacher_id}",
    response_model=teacher_schema.ReadTeacherSchema,
)
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return teacher_crud.crud.destroy(db, teacher_id)


@router.get(
    "/{teacher_id}/courses",
    response_model=list[teacher_schema.ReadTeacherSchema],
)
def get_teachers(
    teacher_id: int,
    db: Session = Depends(dependencies.get_db),
):
    stmt = sa.select(models.Teacher).where(models.Teacher.id == teacher_id)
    teacher = db.scalar(stmt)

    if teacher is None:
        return []

    return teacher.courses
