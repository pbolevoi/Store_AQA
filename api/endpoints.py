HOST = 'https://fakestoreapi.com'


class Endpoints:

    auth = f'{HOST}/auth/login'

    get_products = f'{HOST}/products'
    create_product = f'{HOST}/products'
    def get_product_by_id(self, id): return f'{HOST}/products/{id}'
    def update_product(self, id): return f'{HOST}/products/{id}'
    def delete_product(self, id): return f'{HOST}/products/{id}'

    get_users = f'{HOST}/users'
    create_user = f'{HOST}/users'
    def get_user_by_id(self, id): return f'{HOST}/users/{id}'
    def update_user(self, id): return f'{HOST}/users/{id}'
    def delete_user(self, id): return f'{HOST}/users/{id}'

    carts = f'{HOST}/carts'
    def get_cart_by_id(self, id): return f'{HOST}/carts/{id}'
    def update_cart(self, id): return f'{HOST}/carts/{id}'
    def delete_cart(self, id): return f'{HOST}/carts/{id}'
