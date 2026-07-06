import allure
from ui.pages.base_page import BasePage
from ui.locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):

    @allure.step('Вставка Имени - {first_name}')
    def send_first_name(self, first_name: str):
        self.send_keys(locator=CheckoutLocators.FIRST_NAME, text=first_name)

    @allure.step('Вставка Фамилии - {last_name}')
    def send_last_name(self, last_name: str):
        self.send_keys(locator=CheckoutLocators.LAST_NAME, text=last_name)

    @allure.step('Вставка Почтового кода - {zip_code}')
    def send_zip_code(self, zip_code: str):
        self.send_keys(locator=CheckoutLocators.ZIP_CODE, text=zip_code)

    @allure.step('Нажатие на "Сontinue"')
    def click_continue(self):
        self.click(CheckoutLocators.CONTINUE_BTN)

    @allure.step('Нажатие на "Сancel"')
    def click_cancel(self):
        self.click(CheckoutLocators.CANCEL_BTN)

    @allure.step('Нажатие на "Finish"')
    def click_finish(self):
        self.click(CheckoutLocators.FINISH_BTN)

    @allure.step('Получение суммы товаров')
    def get_total_item_sum(self):
        return self.get_text(CheckoutLocators.ITEM_TOTAL_SUM)

    @allure.step('Получение текста благодарности за заказ')
    def get_text_order_complete(self):
        return self.get_text(CheckoutLocators.TEXT_ORDER_COMPLETE)

    @allure.step('Нажатие на "Back Home"')
    def click_back_home(self):
        self.click(CheckoutLocators.BACK_HOME_BTN)
