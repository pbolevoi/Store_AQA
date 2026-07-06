from api.clients.base_api import BaseAPI
import allure


class CartsAPI(BaseAPI):

    @allure.step('Получение списка корзин')
    def get_carts(self):
        response = self.get(url=self.endpoints.carts)
        self.attach_response(response.json())
        return response

    @allure.step('Создание корзины где userid={userid}, products={products}')
    def create_cart(self, userid, products: list[int]):
        response = self.post(
            url=self.endpoints.carts,
            json=self.payloads.cart_payload(userid, products)
        )
        self.attach_response(response.json())
        return response

    @allure.step('Получение данных корзины где id={id}')
    def get_cart_by_id(self, id):
        response = self.get(url=self.endpoints.get_cart_by_id(id))
        self.attach_response(response.json())
        return response

    @allure.step('Изменение корзины где id={id}, userid={userid}, products={products}')
    def update_cart(self, id, userid, products: list[int]):
        response = self.put(
            url=self.endpoints.update_cart(id),
            json=self.payloads.cart_payload(userid, products)
        )
        self.attach_response(response.json())
        return response

    @allure.step('Удаление корзины по id={id}')
    def delete_cart(self, id):
        response = self.delete(url=self.endpoints.delete_cart(id))
        self.attach_response(response.json())
        return response
