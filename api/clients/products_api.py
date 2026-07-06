from api.clients.base_api import BaseAPI
import allure


class ProductsAPI(BaseAPI):

    @allure.step('Получение списка продуктов')
    def get_products(self):
        response = self.get(url=self.endpoints.get_products)
        self.attach_response(response.json())
        return response

    @allure.step('Создание продукта')
    def create_product(self):
        response = self.post(
            url=self.endpoints.create_product,
            json=self.payloads.product_payload()
        )
        self.attach_response(response.json())
        return response

    @allure.step('Получение данных продукта где id={id}')
    def get_product_by_id(self, id):
        response = self.get(url=self.endpoints.get_product_by_id(id))
        # self.attach_response(response.json())
        return response

    @allure.step('Изменение данных продукта где id={id}')
    def update_product(self, id):
        response = self.put(
            url=self.endpoints.update_product(id),
            json=self.payloads.product_payload()
        )
        self.attach_response(response.json())
        return response

    @allure.step('Удаление продукта где id={id}')
    def delete_product(self, id):
        response = self.delete(url=self.endpoints.delete_product(id))
        self.attach_response(response.json())
        return response
