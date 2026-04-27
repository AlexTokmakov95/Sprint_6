import pytest
import allure
from data import Urls, DataSets
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocator


class TestOrderPage(DataSets):   

    @allure.title('Оформление заказа через кнопку "Заказать вверху страницы"')
    @allure.description('Проверка что при успешном оформлении заказа, появилось всплывающее окно с сообщением об успешном создании заказа ')
    def test_order_page_top_botton_create_order_and__shows_confirmation(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_cookie_accept()
        main_page.click_top_order_button()
        data_sets = DataSets()
        data = data_sets.data_set()
        order_page = OrderPage(driver)
        order_page.fill_user_data(data)
        order_page.go_next()
        order_page.fill_rent_data(data)
        order_page.click_order()
        order_page.click_accept_order()
        base_page = BasePage(driver)
        completed_element = base_page.find_element(OrderPageLocator.order_completed_info, 10)
        assert completed_element.is_displayed(), f"Элемент с локатором {OrderPageLocator.order_completed_info} не найден или не виден на странице."

    @allure.title('Оформление заказа через кнопку "Заказать внизу страницы"')
    @allure.description('Проверка что при успешном оформлении заказа, появилось всплывающее окно с сообщением об успешном создании заказа ')
    def test_order_page_bottom_botton_create_order_and__shows_confirmation(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_cookie_accept()
        main_page.click_bottom_order_button()
        data_sets = DataSets()
        data = data_sets.data_set2()
        order_page = OrderPage(driver)
        order_page.fill_user_data(data)
        order_page.go_next()
        order_page.fill_rent_data(data)
        order_page.click_order()
        order_page.click_accept_order()
        base_page = BasePage(driver)
        completed_element = base_page.find_element(OrderPageLocator.order_completed_info, 10)
        assert completed_element.is_displayed(), f"Элемент с локатором {OrderPageLocator.order_completed_info} не найден или не виден на странице."


