import pytest
from pages.api_post_put_get import ApiRequestsYougile

client = ApiRequestsYougile(
    login="000",
    password="000",
    company_id="000"
    )


@pytest.fixture(scope="module")
def created_project_id():
    response = client.post_project_creation("проект для фикстуры")
    project_id = response.json().get("id")
    return project_id


@pytest.mark.positive
def test_create_project_positive():
    call = client.post_project_creation('проект самый новый')
    assert call.status_code == 201
    assert "id" in call.json()


@pytest.mark.positive
def test_get_project_positive(created_project_id):
    call = client.get_by_id(created_project_id)
    assert call.status_code == 200


@pytest.mark.positive
def test_update_project_positive(created_project_id):
    call = client.put_project(created_project_id, "обнова для фикстуры")
    assert call.status_code == 200


@pytest.mark.negative
def test_create_project_without_title():
    call = client.post_project_creation('')
    assert call.status_code == 400


@pytest.mark.negative
def test_get_project_wrong_id():
    call = client.get_by_id('4f6f0391-0f94-4d30-9b0e-99430a36d4fe')
    assert call.status_code == 404


@pytest.mark.negative
def test_update_project_wrong_id():
    call = client.put_project(
        '4f6f0391-0f94-4d30-9b0e-99430a36d4fe',
        'новое название для несущ-го проекта'
        )
    assert call.status_code == 404
