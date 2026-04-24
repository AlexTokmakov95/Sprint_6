import allure
from data import Urls
from pages.main_page import MainPage


class TestBasePage:

    @allure.title('При нажатии на лого "Яндекс" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка что, на домашней странице при нажатии кнопки "Яндекс" '
                        'происходит корректный редирект на страницу "ЯндексДзен".')
    def test_click_yandex_button_go_to_yandexdzen(self, driver):
        home_page = MainPage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_yandex_button()
        home_page.switch_window(1)
        home_page.wait_url_until_not_about_blank()
        current_url = home_page.current_url()

        assert Urls.url_dzen in current_url

    @allure.title('При нажатии на лого "Самоката" происходит переход на главную страницу "Самоката"')
    @allure.description('Проверка что, на домашней странице при нажатии кнопки "Самоката" '
                        'происходит корректный переход на главную страницу "Самоката".')
    def test_click_scooter_button_go_to_scooter(self, driver):
        home_page = MainPage(driver)
        home_page.go_to_site()
        home_page.click_cookie_accept()
        home_page.click_scooter_button()
        current_url = home_page.current_url()

        assert Urls.url_main_page in current_url