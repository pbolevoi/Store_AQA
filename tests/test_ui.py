import allure
from ui.pages.auth_page import AuthPage
from ui.pages.main_page import MainPage
from ui.pages.cart_page import CartPage
from ui.pages.checkout_page import CheckoutPage


@allure.epic('Авторизация UI')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Вход в аккаунт')
def test_login_and_logout(driver):
    main = MainPage(driver)
    auth = AuthPage(driver)
    auth.open()
    url_before = auth.get_url()
    auth.send_login(username='standard_user')
    auth.send_password(password='secret_sauce')
    auth.click_login()
    url_after = auth.get_url()

    assert url_before != url_after
    main.logout()
    assert url_before == auth.get_url()


@allure.epic('Авторизация UI')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Вход в аккаунт')
def test_login_locked_user(driver):
    auth = AuthPage(driver)
    auth.open()
    current_url = auth.get_url()
    auth.send_login(username='locked_out_user')
    auth.send_password(password='secret_sauce')
    auth.click_login()
    text_error = auth.get_text_error()

    assert current_url == auth.get_url()
    assert text_error.startswith('Epic sadface')


@allure.epic('Авторизация UI')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Вход в аккаунт')
def test_login_without_username(driver):
    auth = AuthPage(driver)
    auth.open()
    current_url = auth.get_url()
    auth.send_login(username='')
    auth.send_password(password='secret_sauce')
    auth.click_login()
    text_error = auth.get_text_error()

    assert current_url == auth.get_url()
    assert text_error.endswith('Username is required')


@allure.epic('Авторизация UI')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Вход в аккаунт')
def test_login_without_password(driver):
    auth = AuthPage(driver)
    auth.open()
    current_url = auth.get_url()
    auth.send_login(username='standard_user')
    auth.send_password(password='')
    auth.click_login()
    text_error = auth.get_text_error()

    assert current_url == auth.get_url()
    assert text_error.endswith('Password is required')


@allure.epic('Авторизация UI')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Вход в аккаунт')
def test_login_with_wrong_password(driver):
    auth = AuthPage(driver)
    auth.open()
    current_url = auth.get_url()
    auth.send_login(username='standard_user')
    auth.send_password(password='secret12345')
    auth.click_login()
    text_error = auth.get_text_error()

    assert current_url == auth.get_url()
    assert text_error.endswith('not match any user in this service')


@allure.epic('Продукт UI')
@allure.feature('Взаимодействие с продуктом')
@allure.story('Добавление продукта в корзину')
def test_add_product_to_cart_on_main_page(driver):
    main = MainPage(driver)
    auth = AuthPage(driver)
    auth.open()
    auth.login('standard_user', 'secret_sauce')
    main.add_to_cart_from_main('Sauce Labs Backpack')

    assert main.counter_cart() == 1

    main.add_to_cart_from_main('Sauce Labs Fleece Jacket')
    main.add_to_cart_from_main('Sauce Labs Onesie')
    main.add_to_cart_from_main('Test.allTheThings() T-Shirt (Red)')

    assert main.counter_cart() == 4
    main.remove_from_main('Sauce Labs Backpack')
    assert main.counter_cart() == 3


@allure.epic('Продукт UI')
@allure.feature('Взаимодействие с продуктом')
@allure.story('Добавление продукта в корзину')
def test_add_product_to_cart_on_product_page(driver):
    main = MainPage(driver)
    auth = AuthPage(driver)
    auth.open()
    auth.login('standard_user', 'secret_sauce')
    main.click_on_the_product('Sauce Labs Backpack')
    name_product = main.get_name_on_product_page()
    price = main.get_price_on_product_page()
    main.add_to_cart_on_product_page()
    main.screenshot()

    assert name_product == 'Sauce Labs Backpack'
    assert price.endswith('29.99')
    assert main.counter_cart() == 1


@allure.epic('Корзина UI')
@allure.feature('Взаимодействие с корзиной')
@allure.story('Добавление и удаление продукта в корзине')
def test_add_to_cart_and_delete_in_cart(driver):
    auth = AuthPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    auth.open()
    auth.login('standard_user', 'secret_sauce')
    main.add_to_cart_from_main('Sauce Labs Bolt T-Shirt')
    main.add_to_cart_from_main('Sauce Labs Fleece Jacket')

    assert main.counter_cart() == 2
    main.open_cart()

    assert cart.product_is_visible('Sauce Labs Bolt T-Shirt')
    cart.remove_product()
    assert main.counter_cart() == 1
    assert not cart.product_is_visible('Sauce Labs Bolt T-Shirt')


@allure.epic('Корзина UI')
@allure.feature('Добавление в корзину и оформление товара')
@allure.story('Оформление товара')
def test_making_an_order(driver):
    auth = AuthPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    auth.open()
    auth.login('standard_user', 'secret_sauce')
    url_on_main = main.get_url()
    main.add_to_cart_from_main('Sauce Labs Backpack')
    main.click_on_the_product('Sauce Labs Onesie')
    main.add_to_cart_on_product_page()

    assert main.counter_cart() == 2
    main.open_cart()
    cart.screenshot()
    assert cart.product_is_visible('Sauce Labs Backpack')
    assert cart.product_is_visible('Sauce Labs Onesie')

    cart.checkout()
    checkout.send_first_name('abc')
    checkout.send_last_name('cba')
    checkout.send_zip_code('123')
    checkout.click_continue()

    assert checkout.get_total_item_sum().endswith('37.98')
    checkout.screenshot()
    checkout.click_finish()
    assert checkout.get_text_order_complete() == 'Thank you for your order!'
    checkout.screenshot()
    checkout.click_back_home()
    assert main.get_url() == url_on_main
