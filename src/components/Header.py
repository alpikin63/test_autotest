from selene.api import s

class Header(object):
    def __init__(self):
        self.login_link = s('a[data-autotest="login"]')
        self.login_name = s('.user-head__username')

    def open_auth(self):
        self.login_link.click()