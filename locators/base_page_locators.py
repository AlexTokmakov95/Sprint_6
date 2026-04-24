from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePageLocator:
    cookie_accept_button = [By.XPATH, ".//button[text()='да все привыкли']"]
    yandex_site_button = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
    scooter_site_button = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]