import sqlalchemy as sa
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import dependencies, models
from crud import assessment_crud
from helpers import general_schemas
from schemas import assessment_schema, student_schema

router = APIRouter()


@router.get(
    "/",
    response_model=general_schemas.ListBaseSchema[
        assessment_schema.ReadAssessmentSchema
    ],
)
def list_assessments(
    db: Session = Depends(dependencies.get_db),
    paginate_params: dict = Depends(dependencies.paginate_params),
):
    return assessment_crud.crud.read_list(
        db,
        skip=paginate_params["skip"],
        limit=paginate_params["limit"],
    )


@router.post(
    "/",
    response_model=assessment_schema.ReadAssessmentSchema,
    status_code=status.HTTP_200_OK,
)
def create_assessment(
    item: assessment_schema.CreateAssessmentSchema,
    db: Session = Depends(dependencies.get_db),
):
    return assessment_crud.crud.create(db, item)


@router.get(
    "/{assessment_id}",
    response_model=assessment_schema.ReadAssessmentSchema,
)
def get_assessment(
    assessment_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return assessment_crud.crud.read_one(db, assessment_id)


@router.put(
    "/{assessment_id}",
    response_model=assessment_schema.ReadAssessmentSchema,
)
def update_assessment(
    item: assessment_schema.CreateAssessmentSchema,
    assessment_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return assessment_crud.crud.update(db, assessment_id, item)


@router.delete(
    "/{assessment_id}",
    response_model=assessment_schema.ReadAssessmentSchema,
)
def delete_assessment(
    assessment_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return assessment_crud.crud.destroy(db, assessment_id)


@router.get(
    "/{assessment_id}/students",
    response_model=list[assessment_schema.ReadAssessmentSchema],
)
def get_students(
    assessment_id: int,
    db: Session = Depends(dependencies.get_db),
):
    stmt = sa.select(models.Assessment).where(models.Assessment.id == assessment_id)
    assessment = db.scalar(stmt)

    if assessment is None:
        return []

    return assessment.students
