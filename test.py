import requests
import pytest


@pytest.mark.parametrize(
    "user_id, email",
    [
        (2, "janet.weaver@reqres.in")
    ]
)
def test_user_data(user_id, email):
    url = f"http://0.0.0.0:8000/api/users/{user_id}"
    try:
        response = requests.get(url)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        body = response.json()
        data = body['data']

        assert data['email'] == email, f"Expected email {email}, but got {data['email']}"
        assert data['id'] == user_id, f"Expected id {user_id}, but got {data['id']}"
    except requests.exceptions.HTTPError as http_err:
        pytest.fail(f"HTTP error occurred: {http_err}")
    except Exception as err:
        pytest.fail(f"Other error occurred: {err}")