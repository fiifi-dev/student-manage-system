from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import dependencies
from crud import student_assessment_crud
from schemas import student_assessment_schema

router = APIRouter()


@router.post(
    "/",
    response_model=student_assessment_schema.ReadStudentAssessmentSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_student_course(
    item: student_assessment_schema.CreateStudentAssessmentSchema,
    db: Session = Depends(dependencies.get_db),
):
    return student_assessment_crud.crud.create(db, item)


@router.put(
    "/{student_course_id}",
    response_model=student_assessment_schema.ReadStudentAssessmentSchema,
)
def update_student_course(
    item: student_assessment_schema.CreateStudentAssessmentSchema,
    student_course_id: int,
    db: Session = Depends(dependencies.get_db),
):

    return student_assessment_crud.crud.update(db, student_course_id, item)


@router.delete(
    "/{student_course_id}",
    response_model=student_assessment_schema.ReadStudentAssessmentSchema,
)
def delete_student_course(
    student_course_id: int,
    db: Session = Depends(dependencies.get_db),
):
    return student_assessment_crud.crud.destroy(db, student_course_id)
