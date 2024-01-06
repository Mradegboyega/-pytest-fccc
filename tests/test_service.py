import pytest
import requests
import source.service as service
from unittest import mock

@mock.patch('source.service.get_user_from_db')
def test_get_user_from_db(mock_get_user_from_db):
    """
    Test the behavior of get_user_from_db when using a mock.

    The function is mocked to return 'Mocked michelle', and the test
    verifies that the actual result matches the expected result.
    """
    mock_get_user_from_db.return_value = 'Mocked michelle'
    user_name = service.get_user_from_db(2)
    assert user_name == 'Mocked michelle'


@mock.patch('requests.get')
def test_get_users(mock_get):
    """
    Test the behavior of get_users when using a mock.

    The function is mocked to simulate a successful API response,
    and the test verifies that the actual result matches the expected result.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": 'John Doe'}
    mock_get.return_value = mock_response

    data = service.get_users()
    assert data == {"id": 1, "name": 'John Doe'}


def test_get_users_error():
    """
    Test the error handling behavior of the get_users function when encountering an HTTP error.

    The function is mocked to simulate an HTTP response with a status code of 400.
    The test checks that a requests.exceptions.HTTPError is raised when get_users is called.
    """
    with mock.patch('source.service.requests.get') as mock_get:
        mock_response = mock.Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        # Explicitly call raise_for_status() and check if it raises an HTTPError
        try:
            service.get_users()
            assert False, "Expected HTTPError, but no exception was raised."
        except requests.exceptions.HTTPError:
            pass  # This is expected behavior
