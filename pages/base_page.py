import allure
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент на странице')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step('Найти элементы на странице')
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.url_main_page
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Подождать перехода на другую вкладку')
    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))
    
    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step('Подождать пока элемент станет кликабелен')
    def wait_before_click(self, element, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))

    @allure.step('Подождать пока элемент станет виден')
    def wait_before_assert(self, element, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((element)))   
        
    
