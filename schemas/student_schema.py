from helpers.general_schemas import PersonSchema


class CreateStudentSchema(PersonSchema):
    pass


class ReadStudentSchema(CreateStudentSchema):
    id: int

    class Config:
        orm_mode = True
