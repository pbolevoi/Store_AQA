from selenium.webdriver.common.by import By


class CartLocators:

    CONTINUE_SHOPPING_BTN = (By.ID, 'continue-shopping')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[id^="remove"]')
    CART_ITEM = (By.CSS_SELECTOR, '.cart_item')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
