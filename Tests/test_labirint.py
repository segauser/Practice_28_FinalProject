# from cd Tests/ :
# python -m pytest -v --driver chrome --driver-path chromedriver.exe test_labirint.py
# python -m pytest -s --driver chrome --driver-path chromedriver.exe --alluredir=test_results/ test_labirint.py

from Pages.labirint import LabirintPage
from config import TestData
import pytest
import allure

@allure.epic("Тесты перехода к соответсвующим страницам")
class Test_ui_link():

    @allure.description("Главная страница")
    @pytest.mark.ui_link
    def test_go_to_main_page(self, web_browser):
        """ Переход на главную страницу """
        page = LabirintPage(web_browser)
        page.LOCATOR_NEWS_LINC.click()
        page.LOCATOR_LOGO.click()
        assert page.get_current_url() == TestData.base_url

    @pytest.mark.ui_link
    def test_clic_icon_postponed(self, web_browser):
        """ Переход по кнопке Отложенное ведет на страницу Отложенное"""
        page = LabirintPage(web_browser)
        page.LOCATOR_ICON_POSTPONED.click()
        assert page.get_current_url() == TestData.postponed_link

    @pytest.mark.ui_link
    def test_delivery_and_payment_linc(self, web_browser):
        """ Переход по ссылке Доставка и оплата ведет на соответствующую страницу """
        page = LabirintPage(web_browser)
        page.LOCATOR_DELIVERY_AND_PAYMENT.click()
        assert page.get_current_url() == TestData.delivery_and_payment_link

    @pytest.mark.ui_link
    def test_certificate_linc(self, web_browser):
        """ Переход по ссылке Сертификаты ведет на соответствующую страницу """
        page = LabirintPage(web_browser)
        page.LOCATOR_CERTIFICATE_LINC.click()
        assert page.get_current_url() == TestData.certificate_link

    @pytest.mark.ui_link
    def test_rating_linc(self, web_browser):
        """ Переход по ссылке Рейтинг ведет на соответствующую страницу """
        page = LabirintPage(web_browser)
        page.LOCATOR_RATING_LINC.click()
        assert page.get_current_url() == TestData.rating_kink

    @pytest.mark.ui_link
    def test_news_linc(self, web_browser):
        """ Переход по ссылке Новинки ведет на соответствующую страницу """
        page = LabirintPage(web_browser)
        page.LOCATOR_NEWS_LINC.click()
        assert page.get_current_url() == TestData.news_link

    @pytest.mark.ui_link
    def test_sale_linc(self, web_browser):
        """ Переход по ссылке Скидки ведет на соответствующую страницу """
        page = LabirintPage(web_browser)
        page.LOCATOR_SALE_LINC.click()
        assert page.get_current_url() == TestData.sale_link

    @pytest.mark.ui_link
    def test_phone_number_linc(self, web_browser):
        """ Переход по ссылке +7 499 920-95-25 """
        page = LabirintPage(web_browser)
        page.LOCATOR_PHONE_NUMBER_LINC.click()
        text = page.LOCATOR_PHONE_NUMBER_BTN.get_text()
        assert text == TestData.text_phone_number

@allure.epic("Тесты элементов шапки страницы")
class Test_ui_head():

    @allure.description("Видимость иконок")
    @pytest.mark.ui_head
    def test_visible_block_icons(self, web_browser):
        """ Блок иконок виден на странице """
        page = LabirintPage(web_browser)
        assert page.LOCATOR_BLOCK_ICONS.is_visible()


    @pytest.mark.ui_head
    def test_clic_icon_messages(self, web_browser):
        """ Название всплывающего окна 'Сообщения' соответствует параметрам неавторизованного пользователя"""
        page = LabirintPage(web_browser)
        page.LOCATOR_ICON_MESSAGES.click()
        text = page.LOCATOR_AUTH_WINDOW.get_text()
        assert text == TestData.text_auth_window


    @pytest.mark.ui_head
    def test_clic_icon_my_maze(self, web_browser):
        """ Название всплывающего окна 'Мой лабиринт' соответствует параметрам неавторизованного пользователя"""
        page = LabirintPage(web_browser)
        page.LOCATOR_ICON_MY_MAZE.click()
        text = page.LOCATOR_AUTH_WINDOW.get_text()
        assert text == TestData.text_auth_window


    @pytest.mark.ui_head
    def test_visible_up_navigation_panel(self, web_browser):
        """ Панель навигации видна на сайте """
        page = LabirintPage(web_browser)
        assert page.LOCATOR_UP_NAVIGATION_PANEL.is_visible()

@allure.epic("Тесты тела страницы")
class Test_ui_body():


    @allure.description("Наличие сертификатов на странице")
    @pytest.mark.ui_body
    def test_certificate_availability(self, web_browser):
        """ Проверяем что на странице сертификаты есть сертификаты """
        page = LabirintPage(web_browser)
        page.LOCATOR_CERTIFICATE_LINC.click()
        page.LOCATORS_CERTIFICATE_TITLES.scroll_to_element()
        # проверим что количество сертификатов равно 8
        assert page.LOCATORS_CERTIFICATE_TITLES.count() == 8


    @pytest.mark.ui_body
    def test_rating_book(self, web_browser):
        """ Проверяем что на странице Рейтинги есть книги по умолчанию 60"""
        page = LabirintPage(web_browser)
        page.LOCATOR_RATING_LINC.click()
        assert page.LOCATORS_RATING_BOOK_TITLE.count() == 60


    @pytest.mark.ui_body
    def test_photo_product(self, web_browser):
        """ Карточки в результатах поиска имеют ссылку на фото"""
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_DYSTOPIA)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        # проверим что атрибут src не пустой
        for src in page.LOCATORS_SEARCH_BOOK_SRC.get_attribute('src'):
            assert src != ''

@allure.epic("Тесты основного функционала страницы")
class Test_ui_main_func():

    @allure.description("Функционал поиска по странице")
    @pytest.mark.ui_main_func
    def test_search_product_adventure(self, web_browser):
        """ Поиск по запросу "Антиутопия" выдает результаты """
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_DYSTOPIA)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        # проверим что на странице 60 карточек книг
        assert page.LOCATORS_SEARCH_BOOK_SRC.count() == 60


    @pytest.mark.ui_main_func
    def test_scroll_page(self, web_browser):
        """ Проверка скроллинга страницы """
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_DYSTOPIA)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        page.LOCATORS_PAGE_NUM_2.scroll_to_element()
        assert page.LOCATORS_PAGE_NUM_2.is_clickable()
        page.LOCATORS_PAGE_NUM_2.highlight_and_make_screenshot('scrolling.png')

@allure.epic("Тесты корзины и избранного")
class Test_ui_cart():

    @allure.description("Добавление в корзину")
    @pytest.mark.ui_cart
    def test_add_book_in_cart(self, web_browser):
        """ Проверка добавления книги в корзину """
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_1984)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        page.LOCATOR_BOOK_1984.click()
        page.LOCATOR_BTN_ADD_TO_CART.click()
        page.LOCATOR_BTN_CART.click()
        # проверим что локатор книги виден в корзине
        assert page.LOCATOR_BOOK_1984.is_visible()
        # проверим что счетчик корзины изменился
        assert page.LOCATOR_COUNTER_CART.get_text() == '1'


    @pytest.mark.ui_cart
    def test_delete_book_in_cart(self, web_browser):
        """ Проверка удаления книги из корзины """
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_1984)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        page.LOCATOR_BOOK_1984.click()
        page.LOCATOR_BTN_ADD_TO_CART.click()
        page.LOCATOR_BTN_CART.click()
        # проверим что локатор книги виден в корзине
        assert page.LOCATOR_BOOK_1984.is_visible()
        # проверим что счетчик корзины изменился
        assert page.LOCATOR_COUNTER_CART.get_text() == '1'
        page.LOCATOR_LINC_CLEAR_TO_CART.click()
        assert page.LOCATOR_COUNTER_CART.get_text() == '0'


    @pytest.mark.ui_cart
    def test_add_book_in_postponed(self, web_browser):
        """ Проверка добавления книги в отложенное """
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_1984)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        page.LOCATOR_BTN_POSTPONED.scroll_to_element()
        page.LOCATOR_BTN_POSTPONED.click()
        page.LOCATOR_ICON_POSTPONED.scroll_to_element()
        assert page.LOCATOR_COUNTER_POSTPONED.get_text() == '1'


    @pytest.mark.ui_cart
    def test_del_book_from_postponed(self, web_browser):
        """ Проверка удаления книги из отложенного """
        page = LabirintPage(web_browser)
        page.LOCATOR_SEARCH_BAR.send_keys(TestData.title_book_BOOK_1984)
        page.LOCATOR_SEARCH_BAR_BTN.click()
        page.LOCATOR_BTN_POSTPONED.scroll_to_element()
        page.LOCATOR_BTN_POSTPONED.click()
        page.wait_page_loaded()
        page.LOCATOR_BTN_POSTPONED.click()
        page.LOCATOR_BTN_DEL_POSTPONED.click()
        page.LOCATOR_ICON_POSTPONED.scroll_to_element()
        assert page.LOCATOR_COUNTER_POSTPONED.get_text() == '0'
