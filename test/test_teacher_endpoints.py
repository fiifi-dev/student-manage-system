from fastapi.testclient import TestClient
from fastapi import status
from endpoints.teacher_endpoints import router
from core.dependencies import get_db
from core.test_database import override_get_db

client = TestClient(router)


teacher = {}

if router.dependency_overrides_provider is not None:
    router.dependency_overrides_provider[get_db] = override_get_db


def test_list_teachers():
    res = client.get("/")
    assert res.status_code == status.HTTP_200_OK


def test_create_teacher():
    res = client.post("/", json=teacher)
    assert res.status_code == status.HTTP_201_CREATED


def test_get_teacher():
    res = client.get("/1")
    assert res.status_code == status.HTTP_200_OK


def test_update_teacher():
    res = client.put("/1", json=teacher)
    assert res.status_code == 201


def test_delete_teacher():
    res = client.delete("/1")
    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_get_students():
    res = client.get("/1/courses")
    assert res.status_code == status.HTTP_200_OK
