import pytest
import allure
from api.models.product_model import ProductModel
from api.models.user_model import UserModel
from api.models.cart_model import CartModel


@allure.epic('Авторизация')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Получение токена')
@allure.title('Auth test')
def test_auth(auth_api):
    response = auth_api.auth_token_api()
    assert response.status_code == 201
    assert type(response.json().get('token')) is str


@allure.epic('Авторизация')
@allure.feature('Взаимодействие с аккаунтом')
@allure.story('Получение токена')
@allure.title('Auth negative test')
def test_auth_negative(auth_api):
    response = auth_api.get_auth_token_api('useruser', 'passpass123')
    assert response.status_code == 403


@allure.epic('Продукт')
@allure.feature('Управление и получение продукта')
@allure.story('Создание продукта')
@allure.title('Create new product')
def test_create_new_product(product_api):
    create_response = product_api.create_product()
    created_product = ProductModel(**create_response.json())
    get_response = product_api.get_product_by_id(created_product.id)

    assert create_response.status_code == 201
    assert created_product.id > 0
    assert created_product.price > 0
    assert created_product.title != ''
    assert get_response.status_code == 200


@allure.epic('Продукт')
@allure.feature('Управление и получение продукта')
@allure.story('Получение продукта')
@allure.title('Get products')
def test_get_products(product_api):
    prod_list = product_api.get_products()
    products = [ProductModel(**item) for item in prod_list.json()]

    for product in products:
        assert product.id > 0
        assert product.title != ''
        assert product.price > 0
        assert product.description != ''
        assert product.image != ''


@allure.epic('Продукт')
@allure.feature('Управление и получение продукта')
@allure.story('Изменение продукта')
@allure.title('Update product')
def test_update_product(product_api):
    get_response = product_api.get_product_by_id(20)
    got_product = ProductModel(**get_response.json())
    update_response = product_api.update_product(20)
    updated_product = ProductModel(**update_response.json())

    assert got_product.id == updated_product.id
    assert got_product.title != updated_product.title
    assert got_product.price != updated_product.price
    assert got_product.description != updated_product.description


@allure.epic('Продукт')
@allure.feature('Управление и получение продукта')
@allure.story('Удаление продукта')
@allure.title('Delete product')
def test_delete_product(product_api):
    response = product_api.delete_product(20)
    product = ProductModel(**response.json())

    assert response.status_code == 200
    assert product.id == 20
    assert product.title != ''
    assert product.price > 0
    assert product.description != ''


@allure.epic('Продукт')
@allure.feature('Управление и получение продукта')
@allure.story('Получение продукта')
@allure.title('Get product by not exist id')
@pytest.mark.xfail(reason='При получении продукта по несуществующему id - status_code = 200, при получении тела ответа - пусто')
def test_get_product_by_not_exist_id(product_api):
    response = product_api.get_product_by_id(999999999)
    assert response.status_code == 400
    assert response.json() == None


@allure.epic('Пользователь')
@allure.feature('Управление и получение данных пользователя')
@allure.story('Создание пользователя')
@allure.title('Create new user')
def test_create_new_user(user_api):
    create_response = user_api.create_user()
    # проблема в api, тело ответа возвращается через раз
    get_response = user_api.get_user_by_id(create_response.json().get('id'))

    assert create_response.status_code == 201
    assert get_response.status_code == 200


@allure.epic('Пользователь')
@allure.feature('Управление и получение данных пользователя')
@allure.story('Получение данных пользователя')
@allure.title('Get users')
def test_get_users(user_api):
    user_list = user_api.get_users()
    user = [UserModel(**item) for item in user_list.json()]

    assert user_list.status_code == 200
    assert user[0].id > 0
    assert user[1].username != ''
    assert user[2].password != ''
    assert user[3].email != ''
    assert user[4].id > 0


@allure.epic('Пользователь')
@allure.feature('Управление и получение данных пользователя')
@allure.story('Update user')
def test_update_user(user_api):
    get_response = user_api.get_user_by_id(10)
    got_user = UserModel(**get_response.json())
    update_response = user_api.update_user(10)
    updated_user = UserModel(**update_response.json())

    assert update_response.status_code == 200
    assert got_user.id == 10
    assert got_user.email != updated_user.email
    assert got_user.username != updated_user.username
    assert got_user.password != updated_user.password


@allure.epic('Пользователь')
@allure.feature('Управление и получение данных пользователя')
@allure.story('Удаление пользователя')
@allure.title('Delete user')
def test_delete_user(user_api):
    response = user_api.delete_user(10)
    user = UserModel(**response.json())

    assert response.status_code == 200
    assert user.id == 10
    assert user.email != None
    assert user.username != ''
    assert user.password != ''


@allure.epic('Пользователь')
@allure.feature('Управление и получение данных пользователя')
@allure.story('Получение данных пользователя')
@allure.title('Get user by not exist id')
@pytest.mark.xfail(reason='При получении user по несуществующему id - status_code = 200, при получении тела ответа - пусто')
def test_get_user_by_not_exist_id(user_api):
    response = user_api.get_user_by_id(999999999)
    assert response.status_code == 400
    assert response.json() == None


@allure.epic('Пользователь')
@allure.feature('Управление и получение данных пользователя')
@allure.story('Удаление пользователя')
@allure.title('Delete user with not exist id')
@pytest.mark.xfail(reason='status_code = 200 при удалении несуществующего user')
def test_delete_user_with_not_exist_id(user_api):
    response = user_api.delete_user(999999999)
    assert response.status_code == 400
    assert response.json() == None


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Создание корзины')
@allure.title('Create cart')
def test_create_cart(cart_api):
    # возвращает только id, userId, products: [{productId}, {productId}]
    create_response = cart_api.create_cart(1, [1, 2])
    created_cart = CartModel(**create_response.json())
    get_response = cart_api.get_cart_by_id(created_cart.id)  # возвращает None

    assert create_response.status_code == 201
    assert get_response.status_code == 200
    assert created_cart.userId == 1
    assert len(created_cart.products) == 2


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Получение данных корзины')
@allure.title('Get carts')
def test_get_carts(cart_api):
    response = cart_api.get_carts()

    assert response.status_code == 200
    assert len(response.json()) > 0


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Получение данных корзины')
@allure.title('Get cart by id')
def test_get_cart_by_id(cart_api):
    response = cart_api.get_cart_by_id(5)
    cart = CartModel(**response.json())

    assert response.status_code == 200
    assert cart.id == 5
    assert cart.userId > 0
    assert cart.products


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Изменение корзины')
@allure.title('Update cart')
def test_update_cart(cart_api):
    get_response = cart_api.get_cart_by_id(1)
    got_cart = CartModel(**get_response.json())
    update_response = cart_api.update_cart(1, 10, [5, 6, 7, 8])
    updated_cart = CartModel(**update_response.json())

    assert get_response.status_code == 200
    assert update_response.status_code == 200
    assert updated_cart.id == got_cart.id
    assert updated_cart.userId != got_cart.userId
    assert updated_cart.userId == 10
    assert len(updated_cart.products) == 4
    assert updated_cart.products[0].productId == 5
    assert updated_cart.products[1].productId == 6
    assert updated_cart.products[2].productId == 7
    assert updated_cart.products[-1].productId == 8


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Удаление корзины')
@allure.title('Delete cart')
def test_delete_cart(cart_api):
    get_response = cart_api.get_cart_by_id(5)
    got_cart = CartModel(**get_response.json())
    del_response = cart_api.delete_cart(5)
    del_cart = CartModel(**del_response.json())

    assert del_response.status_code == 200
    assert got_cart.id == del_cart.id
    assert got_cart.userId == del_cart.userId


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Получение данных корзины')
@allure.title('Get cart by not exist id')
@pytest.mark.xfail(reason='cart с id = 100 не существует, при этом status_code = 200, тело ответа = None')
def test_get_cart_by_not_exist_id(cart_api):
    get_response = cart_api.get_cart_by_id(100)

    assert get_response.status_code == 400
    assert get_response.json() == None


@allure.epic('Корзина')
@allure.feature('Управление и получение данных корзины')
@allure.story('Удаление корзины')
@allure.title('Delete cart with not exist id')
@pytest.mark.xfail(reason='cart с id = 100 не существует, при этом status_code = 200, тело ответа = None')
def test_delete_cart_with_notexist_id(cart_api):
    get_response = cart_api.get_cart_by_id(100)
    del_response = cart_api.delete_cart(100)

    assert del_response.status_code == 400
    assert get_response.json() == None
    assert del_response.json() == None
