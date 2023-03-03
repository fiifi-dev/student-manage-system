from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime


class Base(orm.DeclarativeBase):
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)

    @orm.declared_attr  # type: ignore
    def __tablename__(cls):
        return cls.__name__.lower()


class Person(Base):
    __abstract__ = True

    first_name: orm.Mapped[str] = orm.mapped_column(
        sa.String(100),
        nullable=True,
    )
    last_name: orm.Mapped[str] = orm.mapped_column(
        sa.String(100),
        nullable=True,
    )


class Student(Person):
    assessments: orm.Mapped[List["StudentAssessment"]] = orm.relationship(
        back_populates="student"
    )

    courses: orm.Mapped[List["StudentCourse"]] = orm.relationship(
        back_populates="student"
    )


class Teacher(Person):
    courses: orm.Mapped[List["CourseTeacher"]] = orm.relationship(
        back_populates="teacher",
    )
    assessments: orm.Mapped[List["Assessment"]] = orm.relationship(
        back_populates="teacher",
    )


class Course(Base):
    code: orm.Mapped[str] = orm.mapped_column(sa.String(10), unique=True)
    name: orm.Mapped[str] = orm.mapped_column(sa.String(100), unique=True)

    teachers: orm.Mapped[List["CourseTeacher"]] = orm.relationship(
        back_populates="course",
    )

    students: orm.Mapped[List["StudentCourse"]] = orm.relationship(
        back_populates="course",
    )

    assessments: orm.Mapped[List["Assessment"]] = orm.relationship(
        back_populates="course",
    )


class CourseTeacher(Base):
    course_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("course.id"),
        primary_key=True,
    )
    teacher_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("teacher.id"),
        primary_key=True,
    )

    course: orm.Mapped["Course"] = orm.relationship(back_populates="teachers")
    teacher: orm.Mapped["Teacher"] = orm.relationship(back_populates="courses")

    registered_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=sa.func.now(),
    )


class StudentCourse(Base):
    student_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("student.id"),
        primary_key=True,
    )
    course_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("course.id"),
        primary_key=True,
    )

    student: orm.Mapped["Student"] = orm.relationship(back_populates="courses")
    course: orm.Mapped["Course"] = orm.relationship(back_populates="students")

    registered_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=sa.func.now(),
    )


class Assessment(Base):
    title: orm.Mapped[str] = orm.mapped_column(sa.String(200))
    due_date: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime)
    total_score: orm.Mapped[float] = orm.mapped_column(sa.Float)
    posted_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=sa.func.now(),
    )

    course_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("course.id"))
    course: orm.Mapped[Course] = orm.relationship(back_populates="assessments")

    teacher_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("teacher.id"))
    teacher: orm.Mapped[Teacher] = orm.relationship(back_populates="assessments")

    students: orm.Mapped[List["StudentAssessment"]] = orm.relationship(
        back_populates="assessment",
    )


class StudentAssessment(Base):
    score: orm.Mapped[float] = orm.mapped_column(sa.Float)
    file_link: orm.Mapped[str] = orm.mapped_column(sa.String(150))
    submission_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime,
        default=sa.func.now(),
    )

    assessment_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("assessment.id"),
        primary_key=True,
    )
    student_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("student.id"),
        primary_key=True,
    )

    assessment: orm.Mapped["Assessment"] = orm.relationship(back_populates="students")
    student: orm.Mapped["Student"] = orm.relationship(back_populates="assessments")
