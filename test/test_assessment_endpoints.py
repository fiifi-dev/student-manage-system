from fastapi.testclient import TestClient
from fastapi import status
from endpoints.assessment_endpoints import router
from core.dependencies import get_db
from core.test_database import override_get_db

client = TestClient(router)


assessment = {}

if router.dependency_overrides_provider is not None:
    router.dependency_overrides_provider[get_db] = override_get_db


def test_list_assessments():
    res = client.get("/")
    assert res.status_code == status.HTTP_200_OK


def test_create_assessment():
    res = client.post("/", json=assessment)
    assert res.status_code == status.HTTP_201_CREATED


def test_get_assessment():
    res = client.get("/1")
    assert res.status_code == status.HTTP_200_OK


def test_get_teachers():
    res = client.get("/1/teachers")
    assert res.status_code == status.HTTP_200_OK


def test_update_assessment():
    res = client.put("/1", json=assessment)
    assert res.status_code == 201


def test_delete_assessment():
    res = client.delete("/1")
    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_get_students():
    res = client.put("/1/students", json=assessment)
    assert res.status_code == status.HTTP_200_OK
