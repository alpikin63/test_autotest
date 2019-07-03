from selenium import webdriver
from src.pages.Login import Login
from src.components.Header import Header
from selene.api import *
from src.models.user import User
import allure
from allure_commons.types import AttachmentType

browser.set_driver(webdriver.Chrome('/home/aero/PycharmProjects/test_autotest/chromedriver'))
test_user = User(phone='3777777777', password='Qwerty!23')
uncorrect_user = User(phone='3777777778', password='Qwerty!23')

def setup():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')


def teardown():
    browser.close()


@allure.title('Первый тест')
def test_auth():
    with allure.step('Переход на страницу авторизации'):
        Header().open_auth()
    with allure.step('Ввод логина и пароля'):
        Login().auth(phone=test_user.phone, password=test_user.password)
    with allure.step('Проверка авторизаци пользователя'):
        Header().login_name.should(have.exact_text('test'))
        allure.attach(
            browser.take_screenshot(), name="Страница авторизованного пользователя",
            attachment_type=AttachmentType.PNG)


@allure.title('Второй тест')
def test_auth_uncorrect():
    with allure.step('Переход на страницу авторизации'):
        Header().open_auth()
    with allure.step('Ввод логина и пароля'):
        Login().auth(phone=uncorrect_user.phone, password=uncorrect_user.password)
    with allure.step('Проверка появления сообщения о неудаче'):
        Login().error_message.should(have.exact_text('Неверный номер телефона или пароль.'))
        allure.attach(
            browser.take_screenshot(), name="Страница неавторизованного пользователя",
            attachment_type=AttachmentType.PNG)
