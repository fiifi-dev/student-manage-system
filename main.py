from fastapi import FastAPI


from endpoints import (
    student_endpoints,
    teacher_endpoints,
    course_endpoints,
    assessment_endpoints,
    course_teacher_endpoints,
    student_course_endpoints,
)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(
    student_endpoints.router,
    prefix="/students",
    tags=["students"],
)

app.include_router(
    teacher_endpoints.router,
    prefix="/teachers",
    tags=["teachers"],
)
app.include_router(
    course_endpoints.router,
    prefix="/courses",
    tags=["courses"],
)

app.include_router(
    assessment_endpoints.router,
    prefix="/assessments",
    tags=["assessments"],
)

app.include_router(
    course_teacher_endpoints.router,
    prefix="/course_teachers",
    tags=["course_teachers"],
)
app.include_router(
    student_course_endpoints.router,
    prefix="/student_courses",
    tags=["student_courses"],
)
