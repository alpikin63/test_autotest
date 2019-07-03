from selene.api import s

class Login(object):
    def __init__(self):
        self.phone_input = s('#tel')
        self.password_input = s('[name="pass"]')
        self.auth_button = s('.auth__submit')
        self.error_message = s('.auth__master-error')

    def auth(self, phone, password):
        self.phone_input.set_value(phone)
        self.password_input.set_value(password)
        self.auth_button.click()

