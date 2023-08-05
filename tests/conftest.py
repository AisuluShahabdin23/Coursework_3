import pytest

@pytest.fixture
def test_data():
    return [
        {
            "date": "2019-12-07T06:17:14.634890",
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "id": 114832369,
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "state": "EXECUTED",
            "to": "Счет 35158586384610753655"
        },
        {
            "date": "2019-12-08T22:46:21.935582",
            "description": "Открытие вклада",
            "id": 863064926,
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "state": "EXECUTED",
            "to": "Счет 90424923579946435907"
        },
        {
            "date": "2019-11-19T09:22:25.899614",
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "id": 154927927,
            "operationAmount": {
                "amount": "30153.72",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "state": "EXECUTED",
            "to": "Счет 43241152692663622869"
        },
        {
            "date": "2019-11-13T17:38:04.800051",
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "id": 482520625,
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "state": "cancelled",
            "to": "Счет 46765464282437878125"
        },
        {
            "date": "2019-11-05T12:04:13.781725",
            "description": "Открытие вклада",
            "id": 801684332,
            "operationAmount": {
                "amount": "21344.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "state": "cancelled",
            "to": "Счет 77613226829885488381"
        }
    ]