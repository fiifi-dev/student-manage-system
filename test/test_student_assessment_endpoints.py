from fastapi.testclient import TestClient
from fastapi import status
from endpoints.student_course_endpoints import router
from core.dependencies import get_db
from core.test_database import override_get_db

client = TestClient(router)


student_course = {}

if router.dependency_overrides_provider is not None:
    router.dependency_overrides_provider[get_db] = override_get_db


def test_create_student_course():
    res = client.post("/", json=student_course)
    assert res.status_code == status.HTTP_201_CREATED


def test_update_student_course():
    res = client.put("/1", json=student_course)
    assert res.status_code == 201


def test_delete_student_course():
    res = client.delete("/1")
    assert res.status_code == status.HTTP_204_NO_CONTENT
