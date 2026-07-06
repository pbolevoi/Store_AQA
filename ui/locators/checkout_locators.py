from selenium.webdriver.common.by import By


class CheckoutLocators:

    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')
    CANCEL_BTN = (By.ID, 'cancel')
    FINISH_BTN = (By.ID, 'finish')
    ITEM_TOTAL_SUM = (By.CSS_SELECTOR, '.summary_subtotal_label')
    BACK_HOME_BTN = (By.ID, 'back-to-products')
    TEXT_ORDER_COMPLETE = (By.CSS_SELECTOR, '.complete-header')
