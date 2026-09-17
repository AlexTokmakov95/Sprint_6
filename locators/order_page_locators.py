from selenium import webdriver
from selenium.webdriver.common.by import By


class OrderPageLocator:
    first_name_input = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    last_name_input = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    address_input = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    subway_choose = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]  

    @staticmethod
    def subway_hint_button(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]

    telephone_number_field = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]

    next_button = [By.XPATH, ".//button[text()='Далее']"]
    date_field = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    rental_period_field = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    rental_period_list = [By.XPATH, ".//div[@class='Dropdown-option']"]
    color_choose = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    comment_for_courier_field = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    order_button = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    accept_order_button = [By.XPATH, ".//button[text()='Да']"]
    order_completed_info = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    show_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"]

