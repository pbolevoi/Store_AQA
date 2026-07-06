import allure
from ui.pages.base_page import BasePage
from ui.locators.auth_locators import AuthLocators


class AuthPage(BasePage):

    @allure.step('Вход под пользователем username={username}, password={password}')
    def login(self, username: str, password: str):
        self.send_keys(locator=AuthLocators.USERNAME_INPUT, text=username)
        self.send_keys(locator=AuthLocators.PASSWORD_INPUT, text=password)
        self.click(AuthLocators.LOGIN_BUTTON)

    @allure.step('Вставка username={username}')
    def send_login(self, username: str):
        self.send_keys(locator=AuthLocators.USERNAME_INPUT, text=username)

    @allure.step('Вставка password={password}')
    def send_password(self, password: str):
        self.send_keys(locator=AuthLocators.PASSWORD_INPUT, text=password)

    @allure.step('Нажатие на login')
    def click_login(self):
        self.click(AuthLocators.LOGIN_BUTTON)

    @allure.step('Получение текста ошибки')
    def get_text_error(self):
        return self.get_text(AuthLocators.TEXT_ERROR)
