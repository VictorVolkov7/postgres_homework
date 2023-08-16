from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent
CUSTOMERS_DATA_PATH = ROOT_PATH.joinpath('north_data', 'customers_data.csv')
EMPLOYEES_DATA_PATH = ROOT_PATH.joinpath('north_data', 'employees_data.csv')
ORDERS_DATA_PATH = ROOT_PATH.joinpath('north_data', 'orders_data.csv')
