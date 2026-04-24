from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPageLocators:
    top_order_button = [By.CLASS_NAME, "Button_Button__ra12g"]
    order_status_button = [By.CLASS_NAME, "Header_Link__1TAG7"]
    bottom_order_button = [By.CLASS_NAME, "Button_Middle__1CSJM"]
    question_buttons = [By.XPATH, ".//div[@class='accordion__button']"]
    answer_texts = [By.CSS_SELECTOR, ".accordion__panel > p"]

    @staticmethod
    def question_button(question_number):
        return [By.XPATH, f".//div[@id='accordion__heading-{question_number}']"]


    @staticmethod
    def answer_text(answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]
    
