import allure
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainLocators


class MainPage(BasePage):

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.click(MainLocators.BURGER_MENU_BUTTON)
        self.click(MainLocators.LOGOUT_BUTTON)

    @allure.step('Открытие корзины')
    def open_cart(self):
        self.click(MainLocators.CART_BUTTON)

    @allure.step('Переход на страницу продукта {product_name}')
    def click_on_the_product(self, product_name: str):
        list_products = self.find_all(MainLocators.ALL_PRODUCTS)
        for product in list_products:
            name_element = product.find_element(*MainLocators.PRODUCT_NAME)
            if product_name in name_element.text:
                name_element.click()
                return

    @allure.step('Добавление продукта {product_name} в корзину на главной странице')
    def add_to_cart_from_main(self, product_name: str):
        list_products = self.find_all(MainLocators.ALL_PRODUCTS)
        for product in list_products:
            name_element = product.find_element(*MainLocators.PRODUCT_NAME)
            if product_name in name_element.text:
                to_id = 'add-to-cart-' + product_name.lower().replace(' ', '-')
                product.find_element(By.ID, to_id).click()
                return
        raise ValueError(f"Продукт с текстом '{product_name}' не найден")

    @allure.step('Удаление продукта {product_name} из корзины на главной странице')
    def remove_from_main(self, product_name: str):
        list_products = self.find_all(MainLocators.ALL_PRODUCTS)
        for product in list_products:
            name_element = product.find_element(*MainLocators.PRODUCT_NAME)
            if product_name in name_element.text:
                to_id = 'remove-' + product_name.lower().replace(' ', '-')
                product.find_element(By.ID, to_id).click()
                return
        raise ValueError(f"Продукт с текстом '{product_name}' не найден")

    @allure.step('Добавление продукта в корзину')
    def add_to_cart_on_product_page(self):
        self.click(MainLocators.ADD_TO_CART_BUTTON)

    @allure.step('Удаление продукта из корзины на странице продукта')
    def remove_on_product_page(self):
        self.click(MainLocators.REMOVE_BUTTON)

    @allure.step('Получение цены продукта на странице продукта')
    def get_price_on_product_page(self):
        return self.get_text(MainLocators.PRODUCT_PRICE)

    @allure.step('Получение названия продукта на странице продукта')
    def get_name_on_product_page(self):
        return self.get_text(MainLocators.PRODUCT_NAME_ON_PAGE)

    @allure.step('Получение кол-ва товара в корзине')
    def counter_cart(self):
        try:
            return int(self.get_text(MainLocators.COUNTER_CART))
        except:
            return 0
