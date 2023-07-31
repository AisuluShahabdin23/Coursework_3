import json
from datetime import date


def get_data():
    """
    Возвращает список транзаций из json-файла
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    """
    Возвращает список, который содержит все непустые и "EXECUTED" транзакции
    """
    filter_data = []
    for d in data:
        if 'state' in d:
            if d['state'] == 'EXECUTED':
                filter_data.append(d)
    return filter_data


def get_last_values(data, count_last_values):
    """
    Возвращает 5 последних выполненных(EXECUTED)операций
    """
    data_ = sorted(data, key=lambda x: x["date"], reverse=True)
    data_ = data_[:count_last_values]
    return data_



def get_date(operations) -> str:
    """
    Возвращает дату транзакции в формате - ДД.ММ.ГГГГ
    """
    normal_date = date.fromisoformat(operations["date"][:10])
    strtime_date = normal_date.strftime("%d.%m.%Y")
    return strtime_date


def encoding_from(operations: dict):
    from_name, from_account = operations["from"].rsplit(" ", 1)
    if len(from_account) == 16:
        encoding_from_account = f'{from_account[:4]} {from_account[4:6]}** **** {from_account[-4:]}'
    else:
        encoding_from_account = f'**{from_account[-4:]}'
    encoding_from = from_name + " " + encoding_from_account
    return encoding_from


def encoding_to(operations: dict):
    to_name, to_account = operations["to"].rsplit(" ", 1)
    if len(to_account) == 16:
        encoding_to_account = f'{to_account[:4]} {to_account[4:6]}** **** {to_account[-4:]}'
    else:
        encoding_to_account = f'**{to_account[-4:]}'
    encoding_to = to_name + " " + encoding_to_account
    return encoding_to


def get_amount(operations: dict):
    amount = f'{operations["operationAmount"]["amount"]} ' \
             f'{operations["operationAmount"]["currency"]["name"]} '
    return amount
