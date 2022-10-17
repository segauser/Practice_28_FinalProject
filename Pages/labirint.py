import os
from Pages.base import WebPage
from Pages.elements import WebElement, ManyWebElements


class LabirintPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)


# -------------------------------------- локаторы корзины ------------------------------------------------

    # кнопка добавить в корзину
    LOCATOR_BTN_ADD_TO_CART = WebElement(css_selector='.btn.btn-small.btn-primary.btn-buy')

    # локатор очистить корзину
    LOCATOR_LINC_CLEAR_TO_CART = WebElement(css_selector='.text-regular.empty-basket-link')

    # локатор корзины
    LOCATOR_BTN_CART = WebElement(css_selector='.b-header-b-personal-e-list-item.have-dropdown.last-child')

    # локатор счетчика корзины
    LOCATOR_COUNTER_CART = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')


# ---------------------------------- локаторы панели навигации в шапке сайта ----------------------------------------

    # Лого Лабиринт
    LOCATOR_LOGO = WebElement(class_name='b-header-b-logo-e-logo')

    # верхняя панель навигации
    LOCATOR_UP_NAVIGATION_PANEL = WebElement(class_name='b-header-b-menu-e-list')

    # ссылка доставка и оплата
    LOCATOR_DELIVERY_AND_PAYMENT = WebElement(xpath='//a[@href="/help/" and @class="b-header-b-sec-menu-e-link"]')

    # ссылка сертификаты
    LOCATOR_CERTIFICATE_LINC = WebElement(xpath='//a[@href="/top/certificates/" and '
                                                '@class="b-header-b-sec-menu-e-link"]')
    # ссылка рейтинги
    LOCATOR_RATING_LINC = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')

    # ссылка новинки
    LOCATOR_NEWS_LINC = WebElement(xpath='//a[@href="/novelty/"]')

    # ссылка скидки
    LOCATOR_SALE_LINC = WebElement(xpath='//a[@href="/sale/"]')

    # ссылка телефонного номера
    LOCATOR_PHONE_NUMBER_LINC = WebElement(css_selector='.b-header-b-sec-menu-e-list-'
                                                        'item.have-dropdown.have-dropdown-clickable.analytics-click-js')
    # кнопка вызова по телефону
    LOCATOR_PHONE_NUMBER_BTN = WebElement(xpath='//*[@id="_support_call_number"]/a')


# ----------------------------------- локаторы иконок справа от строки поиска ---------------------------------------

    # блок иконок
    LOCATOR_BLOCK_ICONS = WebElement(css_selector='.b-header-b-personal')

    # иконка сообщения
    LOCATOR_ICON_MESSAGES = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                    'have-dropdown-touchlink.top-link-main_notification')
    # иконка мой лабиринт
    LOCATOR_ICON_MY_MAZE = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.'
                                                   'top-link-main_cabinet.js-b-autofade-wrap')
    # иконка отложено
    LOCATOR_ICON_POSTPONED = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_putorder')

    # локатор счетчика отложено
    LOCATOR_COUNTER_POSTPONED = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in'
                                                        '-dreambox-a')

    # локатор всплывающего окна сообщения
    LOCATOR_AUTH_WINDOW = WebElement(xpath='//div[@class="js-auth__title new-auth__title" and contains'
                                           ' (text(),"Полный доступ к Лабиринту")]')

# ------------------------------------------- локаторы тела страницы ----------------------------------------------

    # страница 2
    LOCATORS_PAGE_NUM_2 = WebElement(xpath='//a[@class="pagination-number__text" and @href="?stype=0&page=2"]')

    # локатор изображения книги
    LOCATOR_BOOK_1984 = WebElement(xpath='//img[@src="https://img4.labirint.ru/rc/95b18bd674e3077442d0f3e7ad53f957'
                                         '/363x561q80/books80/790566/cover.png?1618316737"]')

    # кнопка сердечко Отложено
    LOCATOR_BTN_POSTPONED = WebElement(xpath='//a[@data-id_book="790566" and @data-hasqtip="0"]')

    # кнопка сердечко Отложено удаление
    LOCATOR_BTN_DEL_POSTPONED = WebElement(xpath='//span[@class ="b-list-item-hover pointer"]')


# ---------------------------------------- локаторы строки поиска -----------------------------------------

    LOCATOR_SEARCH_BAR = WebElement(id='search-field')
    LOCATOR_SEARCH_BAR_BTN = WebElement(class_name='b-header-b-search-e-btn')

# --------------------------------------------- локаторы группы элементов ---------------------------------------------

    # локатор всех элементов из поиска
    LOCATORS_SEARCH_BOOK_SRC = ManyWebElements(class_name='book-img-cover')

    # локатор всех элементов из поиска
    LOCATORS_CERTIFICATE_TITLES = ManyWebElements(class_name='genres-carousel__item')

    # локатор всех элементов из поиска
    LOCATORS_RATING_BOOK_TITLE = ManyWebElements(css_selector='.product.need-watch')





