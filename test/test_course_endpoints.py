from fastapi.testclient import TestClient
from fastapi import status
from endpoints.course_endpoints import router
from core.dependencies import get_db
from core.test_database import override_get_db

client = TestClient(router)


course = {}

if router.dependency_overrides_provider is not None:
    router.dependency_overrides_provider[get_db] = override_get_db


def test_list_courses():
    res = client.get("/")
    assert res.status_code == status.HTTP_200_OK


def test_create_course():
    res = client.post("/", json=course)
    assert res.status_code == status.HTTP_201_CREATED


def test_get_course():
    res = client.get("/1")
    assert res.status_code == status.HTTP_200_OK


def test_get_teachers():
    res = client.get("/1/teachers")
    assert res.status_code == status.HTTP_200_OK


def test_update_course():
    res = client.put("/1", json=course)
    assert res.status_code == 201


def test_delete_course():
    res = client.delete("/1")
    assert res.status_code == status.HTTP_204_NO_CONTENT


def test_get_students():
    res = client.put("/1/students", json=course)
    assert res.status_code == status.HTTP_200_OK


def test_download_assessment_file():
    res = client.put("/1", json=course)
    assert res.status_code == status.HTTP_200_OK
