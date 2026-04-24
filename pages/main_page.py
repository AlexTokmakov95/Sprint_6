import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(MainPageLocators.top_order_button).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(MainPageLocators.bottom_order_button).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(MainPageLocators.question_buttons, 10)
        target_elem = elems[question_number]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_elem)
        time.sleep(0.5) 
        return target_elem.click()  

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти на страницу ЯндексДзен')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.yandex_site_button).click()
    
    @allure.step('Перейти на страницу Самоката')
    def click_scooter_button(self):
        return self.find_element(BasePageLocator.scooter_site_button).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.cookie_accept_button).click()                         


