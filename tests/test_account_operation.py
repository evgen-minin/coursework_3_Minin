from account_operations.src.models.account_operation import Operation


def test_encode_from_to():
    operation = Operation(1, 'EXECUTED', '2019-08-26T10:50:58.294041',
                          {'amount': '31957', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'Перевод организации',
                          'Maestro 1596837868705199', 'Счет 64686473678894779589')
    assert operation.encode_from_to('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert operation.encode_from_to('Счет 64686473678894779589') == 'Счет **9589'


def test_str():
    operation = Operation(1, 'EXECUTED', '2019-08-26T10:50:58.294041',
                          {'amount': '31957', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'Перевод организации',
                          'Maestro 1596837868705199', 'Счет 64686473678894779589')
    assert operation.__str__() == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.00 руб.'
