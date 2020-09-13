import json

import pytest

from src.app import sum_range

test_sum_range_data = [6]
test_total_data = [({"total": 50000005000000})]
test_total_invalid_data = [({"total": 123})]


@pytest.mark.parametrize("expected_output", test_sum_range_data)
def test_sum_range(expected_output):
    numbers_to_add = list(range(4))
    actual_output = sum_range(numbers_to_add[0], numbers_to_add[-1])
    assert actual_output == expected_output


@pytest.mark.parametrize("expected_output", test_total_data)
def test_total(app, client, expected_output):
    res = client.get('/total')
    assert res.status_code == 200
    assert expected_output == json.loads(res.get_data(as_text=True))


@pytest.mark.parametrize("not_expected_output", test_total_invalid_data)
def test_total_invalid(app, client, not_expected_output):
    res = client.get('/total')
    assert res.status_code == 200
    assert not_expected_output != json.loads(res.get_data(as_text=True))


def test_total_invalid_url(app, client):
    res = client.get('/')
    assert res.status_code == 404
