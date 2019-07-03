from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''Инициализация драйвера'''
driver = webdriver.Chrome('/home/aero/PycharmProjects/test_autotest/chromedriver')
driver.maximize_window()
driver.get('http://loginarea:passarea@nspk.aeroidea.ru')

'''Ввод логина и пароля'''
driver.find_element_by_css_selector('a[data-autotest="login"]').click()
driver.find_element_by_css_selector('#tel').send_keys('3777777777')
driver.find_element_by_css_selector('[name="pass"]').send_keys('Qwerty!23')

'''Нажатие кнопки отправить'''
driver.find_element_by_css_selector('.auth__submit').click()

'''Проверка на авторизацию пользователем'''
assert WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.user-head__username'))).text == 'test'


driver.close()