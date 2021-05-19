import pytest
from .mock_data import data_mock
from requests import get, post, put, delete, patch


domain_url = "http://challengeqa.staging.devmuch.io/en/"


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], 200)

        for data in data_mock
        if data["is_valid"]
    ]
)
def test_request_with_content_argument_should_return_200_satus_code(test_input, expected_return):
    full_url = domain_url + test_input
    assert get(full_url).status_code == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], 405)

        for data in data_mock
    ]
)
def test_request_post_with_any_argument_should_return_405_not_allowed(test_input, expected_return):
    full_url = domain_url + test_input
    assert post(full_url).status_code == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], 405)

        for data in data_mock
    ]
)
def test_request_put_with_any_argument_should_return_405_not_allowed(test_input, expected_return):
    full_url = domain_url + test_input
    assert put(full_url).status_code == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], 405)

        for data in data_mock
    ]
)
def test_request_patch_with_any_argument_should_return_405_not_allowed(test_input, expected_return):
    full_url = domain_url + test_input
    assert patch(full_url).status_code == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], 405)

        for data in data_mock
    ]
)
def test_request_delete_with_any_argument_should_return_405_not_allowed(test_input, expected_return):
    full_url = domain_url + test_input
    assert delete(full_url).status_code == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], 400)

        for data in data_mock
        if not data["is_valid"]
    ]
)
def test_request_with_invalid_argument_should_return_400_bad_request(test_input, expected_return):
    full_url = domain_url + test_input
    assert get(full_url).status_code == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], data["expected_content_en"])
        
        for data in data_mock
        if data["is_valid"]
    ]
)
def test_request_in_portuguese_when_argument_is_valid_should_return_expected_json_content(test_input, expected_return):
    full_url = domain_url + test_input
    assert get(full_url).content == expected_return


@pytest.mark.parametrize(
    "test_input, expected_return",
    [
        (data["argument"], data["expected_content_en"])

        for data in data_mock
        if not data["is_valid"]
    ]
)
def test_request_in_portuguese_with_invalid_argument_should_return_expected_json_content(test_input, expected_return):
    full_url = domain_url + test_input
    assert get(full_url).content == expected_return


