from selenium import webdriver
from src.pages.Login import Login
from src.components.Header import Header
from selene.api import *
from src.models.user import User

browser.set_driver(webdriver.Chrome('/home/aero/PycharmProjects/test_autotest/chromedriver'))
test_user = User(phone='3777777777', password='Qwerty!23')
uncorrect_user = User(phone='3777777778', password='Qwerty!23')

def setup():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')


def teardown():
    browser.close()


def test_auth():
    Header().open_auth()
    Login().auth(phone=test_user.phone, password=test_user.password)
    Header().login_name.should(have.exact_text('test'))

def test_auth_uncorrect():
    Header().open_auth()
    Login().auth(phone=uncorrect_user.phone, password=uncorrect_user.password)
    Login().error_message.should(have.exact_text('Неверный номер телефона или пароль.'))
