import pytest
from src.utils import get_data, get_last_values, get_filtered_data, get_formatted_data

def test_get_data():
    data = get_data()
    assert type(data) == list, 'test_get_data возвращает не словарь'


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert [x['date'] for x in data] == ['2019-12-07T06:17:14.634890', '2019-12-08T22:46:21.935582',
                                         '2019-11-19T09:22:25.899614']


def test_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x['date'] for x in data] == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890',
                                         '2019-11-19T09:22:25.899614']


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    print(data)

