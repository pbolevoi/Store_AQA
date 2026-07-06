from selenium.webdriver.common.by import By


class AuthLocators:

    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    TEXT_ERROR = (By.CSS_SELECTOR, '[data-test="error"]')
