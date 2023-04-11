from account_operations.settings import OPERATIONS
from account_operations.src.models.database import Data


def main():
    database = Data(OPERATIONS)
    data = database.get_data()
    database.get_result(data)


if __name__ == '__main__':
    main()
