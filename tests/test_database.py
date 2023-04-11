from account_operations.settings import OPERATIONS
from account_operations.src.models.account_operation import Operation
from account_operations.src.models.database import Data


def test_data_exists():
    data = Data(OPERATIONS).get_data()
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


def test_get_operation_list(valid_data):
    operation_list = Data(OPERATIONS).get_operations(valid_data)
    assert isinstance(operation_list, list)
    assert isinstance(operation_list[0], Operation)
    assert len(operation_list) == 2
    assert operation_list[1].id == valid_data[1]['id']


def test_get_first_five_sorted_operations(valid_data):
    operation_list = Data(OPERATIONS).get_five_operations(valid_data)
    assert isinstance(operation_list, list)
    assert isinstance(operation_list[0], Operation)
    assert len(operation_list) == 2
    assert operation_list[1].id == valid_data[0]['id']


def test_get_result(valid_data):
    operation_successfully = Data(OPERATIONS).get_result(valid_data)
    assert operation_successfully is True
