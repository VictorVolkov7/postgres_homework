"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2

from settings import ORDERS_DATA_PATH, CUSTOMERS_DATA_PATH, EMPLOYEES_DATA_PATH


def instantiate_from_csv(path):
    """
    Функция дла получения данных из файла
    """
    data_list = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)

        for dict_product in reader:
            dict_product: dict
            data_list.append(dict_product)
        return data_list


# Блок для открытия базы данных и добавления данных в ранее созданные таблицы
psql_pass = os.getenv('PSQL_PASS')
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=psql_pass)
try:
    with conn:
        with conn.cursor() as cur:
            employees_data = instantiate_from_csv(EMPLOYEES_DATA_PATH)
            for emp_data in employees_data:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (emp_data['employee_id'],
                                                                                      emp_data['first_name'],
                                                                                      emp_data['last_name'],
                                                                                      emp_data['title'],
                                                                                      emp_data['birth_date'],
                                                                                      emp_data['notes']))

            customers_data = instantiate_from_csv(CUSTOMERS_DATA_PATH)
            for cust_data in customers_data:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (cust_data['customer_id'],
                                                                          cust_data['company_name'],
                                                                          cust_data['contact_name']))

            orders_data = instantiate_from_csv(ORDERS_DATA_PATH)
            for ord_data in orders_data:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (ord_data['order_id'],
                                                                               ord_data['customer_id'],
                                                                               ord_data['employee_id'],
                                                                               ord_data['order_date'],
                                                                               ord_data['ship_city'],))
finally:
    conn.close()
