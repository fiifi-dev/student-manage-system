from fastapi.testclient import TestClient
from fastapi import status
from endpoints.course_teacher_endpoints import router
from core.dependencies import get_db
from core.test_database import override_get_db

client = TestClient(router)


course_teacher = {}

if router.dependency_overrides_provider is not None:
    router.dependency_overrides_provider[get_db] = override_get_db


def test_create_course_teacher():
    res = client.post("/", json=course_teacher)
    assert res.status_code == status.HTTP_201_CREATED


def test_update_course_teacher():
    res = client.put("/1", json=course_teacher)
    assert res.status_code == 201


def test_delete_course_teacher():
    res = client.delete("/1")
    assert res.status_code == status.HTTP_204_NO_CONTENT
