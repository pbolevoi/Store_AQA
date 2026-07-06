import pytest
from selenium import webdriver
from api.clients.products_api import ProductsAPI
from api.clients.users_api import UserAPI
from api.clients.auth_api import AuthAPI
from api.clients.carts_api import CartsAPI


@pytest.fixture
def product_api():
    api = ProductsAPI()
    yield api
    api.close()


@pytest.fixture
def user_api():
    user = UserAPI()
    yield user
    user.close()


@pytest.fixture
def auth_api():
    auth = AuthAPI()
    yield auth
    auth.close()


@pytest.fixture
def cart_api():
    cart = CartsAPI()
    yield cart
    cart.close()


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    yield browser
    if browser != None:
        browser.quit()
