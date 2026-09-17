class Urls:
    url_main_page = 'https://qa-scooter.praktikum-services.ru/'
    url_order_page = 'https://qa-scooter.praktikum-services.ru/order'
    url_order_status_page = 'https://qa-scooter.praktikum-services.ru/track'
    url_dzen = 'dzen.ru'

class MainPageAnswers:
    answer1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    answer2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    answer3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    answer4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    answer5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    answer6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    answer7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    answer8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

class DataSets:
    def data_set(self):
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

    def data_set2(self):
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





