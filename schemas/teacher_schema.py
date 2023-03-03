from helpers.general_schemas import PersonSchema


class CreateTeacherSchema(PersonSchema):
    pass


class ReadTeacherSchema(CreateTeacherSchema):
    id: int

    class Config:
        orm_mode = True
