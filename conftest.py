import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def data_set():
    return {
        'data_set': {
            'first_name': 'Иван',
            'last_name': 'Иванович',
            'address': 'Иванова улица',
            'subway_name': 'Беляево',
            'telephone_number': '74546524958',
            'date': '15.05.2024',
            'rental_period': 0,
            'color': [0],
            'comment_for_courier': 'Жду возле аптеки',
            'description': 'Корректные данные'  
        }}    


@pytest.fixture
def data_set2():
    return {
        'data_set': {
            'first_name': 'Тест',
            'last_name': 'Тестович',
            'address': 'Тестовая улица',
            'subway_name': 'Лубянка',
            'telephone_number': '79194136055',
            'date': '24.04.2026',
            'rental_period': 1,
            'color': [0, 1],
            'comment_for_courier': 'Очень жду',
            'description': 'Корректные данные'  
        }}   