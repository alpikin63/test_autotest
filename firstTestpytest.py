from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

def setup():

    global driver
    driver = webdriver.Chrome('/home/aero/PycharmProjects/test_autotest/chromedriver')
    driver.get('http://loginarea:passarea@nspk.aeroidea.ru')
    driver.maximize_window()

def teardown():
    driver.close()

def test_auth():

    driver.find_element_by_css_selector('a[data-autotest="login"]').click()
    driver.find_element_by_css_selector('#tel').send_keys('3777777777')
    driver.find_element_by_css_selector('[name="pass"]').send_keys('Qwerty!23')
    driver.find_element_by_css_selector('.auth__submit').click()
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.user-head__username'))).text == 'test'


def test_auth_uncorrect():
    driver.find_element_by_css_selector('a[data-autotest="login"]').click()
    driver.find_element_by_css_selector('#tel').send_keys('3777777778')
    driver.find_element_by_css_selector('[name="pass"]').send_keys('Qwerty!23')
    driver.find_element_by_css_selector('.auth__submit').click()
    time.sleep(2)
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.auth__master-error'))).text == 'Неверный номер телефона или пароль.'






