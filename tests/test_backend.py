from starlette.testclient import TestClient
import json

# import pytest
from backend.main import app


client = TestClient(app)


def test_process_text(test_app, monkeypatch):
    test_request_payload = {
        "text": "test text",
        "description": "test description",
    }
    test_response_payload = {
        "text": "test text",
        "description": "test description",
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(app, "post", mock_post)
    response = test_app.post(
        "/process_text/",
        data=json.dumps(test_request_payload),
    )

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_process_text_invalid_json(test_app):
    response = test_app.post(
        "/process_text/", data=json.dumps({"title": "something"})
    )
    assert response.status_code == 422


def test_generate_report(test_app, monkeypatch):
    test_request_payload = {
        "text": "test text",
        "description": "test description",
    }
    test_response_payload = {
        "text": "test text",
        "description": "test description",
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(app, "post", mock_post)
    response = test_app.post(
        "/generate_report/",
        data=json.dumps(test_request_payload),
    )

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_generate_report_invalid_json(test_app):
    response = test_app.post(
        "/generate_report/", data=json.dumps({"title": "something"})
    )
    assert response.status_code == 422
