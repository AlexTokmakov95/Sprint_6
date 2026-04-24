import pytest
import allure
from pages.main_page import MainPage
from data import MainPageAnswers
from locators.main_page_locators import MainPageLocators


class TestMainPage:
    @allure.title('При нажатии на вопрос раскрывается ответ')
    @allure.description('Проверка что при нажатии на стрелочку вопроса в блоке "Вопросы о важном", '
                        'данный вопрос раскрывается и текст в нем соответствует ТЗ')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, MainPageAnswers.answer1),
            (1, 1, MainPageAnswers.answer2),
            (2, 2, MainPageAnswers.answer3),
            (3, 3, MainPageAnswers.answer4),
            (4, 4, MainPageAnswers.answer5),
            (5, 5, MainPageAnswers.answer6),
            (6, 6, MainPageAnswers.answer7),
            (7, 7, MainPageAnswers.answer8),
        ]
    )
    def test_accardion_click_question_show_answer(self, driver, question, answer, expected_answer):
        ya_scooter_home_page = MainPage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(MainPageLocators.answer_text(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '