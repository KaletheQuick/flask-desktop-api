from application.app import app
from pytest import fixture
from flask import Response

@fixture
def client():
    with app.test_client() as testClient:
        yield testClient

def test_indexGet(client):
    response:Response = client.get("/")
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

def test_chopTest(client):

    response:Response = client.post("/test", json={
        "string_to_cut": "iamyourlyftdriver",
        })
    assert response.status_code == 200
    assert response.json == {"return_string": "muydv"}
    
def test_chopTest_missingDictKey(client):

    response:Response = client.post("/test", json={
        "incorrectData": "iamyourlyftdriver",
        })
    assert response.status_code == 400


def test_chopTest_badContent(client):

    response:Response = client.post("/test", data="This is incorrect data")
    assert response.status_code == 400
    