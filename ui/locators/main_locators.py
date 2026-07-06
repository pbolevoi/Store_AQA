from selenium.webdriver.common.by import By


class MainLocators:

    CART_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')
    ALL_PRODUCTS = (By.CSS_SELECTOR, '.inventory_item')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, '.inventory_details_name')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart')
    REMOVE_BUTTON = (By.ID, 'remove')
    COUNTER_CART = (By.CSS_SELECTOR, '.shopping_cart_badge')
    BURGER_MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.inventory_details_price')
