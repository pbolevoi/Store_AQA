import allure
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.cart_locators import CartLocators


class CartPage(BasePage):

    @allure.step('Нажатие на "Continue Shopping"')
    def click_continue_shopping(self):
        self.click(CartLocators.CONTINUE_SHOPPING_BTN)

    @allure.step('Нажатие на "Checkout"')
    def checkout(self):
        self.click(CartLocators.CHECKOUT_BUTTON)

    @allure.step('Нажатие на "Remove"')
    def remove_product(self):
        self.click(CartLocators.REMOVE_BUTTON)

    @allure.step('Удаление продукта из корзины, где product_name={product_name}')
    def remove_product_by_name(self, product_name: str):
        product_list = self.find_all(CartLocators.CART_ITEM)
        for product in product_list:
            if product_name in product.find_element(*CartLocators.PRODUCT_NAME).text:
                to_id = 'remove-' + product_name.lower().replace(' ', '-')
                product.find_element(By.ID, to_id).click()
                return

    @allure.step('Проверка видимости продукта в корзине, product_name={product_name}')
    def product_is_visible(self, product_name: str):
        product_list = self.find_all(CartLocators.CART_ITEM)
        for product in product_list:
            if product_name in product.find_element(*CartLocators.PRODUCT_NAME).text:
                return True
        return False
