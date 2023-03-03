import sqlalchemy as sa
from core import models
from helpers.crud import BaseCrud
from core import models
from schemas import assessment_schema


class AssessmentCrud(
    BaseCrud[
        models.Assessment,
        assessment_schema.CreateAssessmentSchema,
        assessment_schema.CreateAssessmentSchema,
    ]
):
    pass


crud = AssessmentCrud(models.Assessment)
