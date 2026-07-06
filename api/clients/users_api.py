from api.clients.base_api import BaseAPI
import allure


class UserAPI(BaseAPI):

    @allure.step('Получение списка данных пользователей')
    def get_users(self):
        return self.get(url=self.endpoints.get_users)

    @allure.step('Изменение данных пользователя')
    def create_user(self):
        response = self.post(
            url=self.endpoints.create_user,
            json=self.payloads.user_payload()
        )
        return response

    @allure.step('Получение данных пользователя где id={id}')
    def get_user_by_id(self, id):
        return self.get(url=self.endpoints.get_user_by_id(id))

    @allure.step('Изменение данных пользователя где id={id}')
    def update_user(self, id):
        response = self.put(
            url=self.endpoints.update_user(id),
            json=self.payloads.user_payload()
        )
        return response

    @allure.step('Удаление пользователя по id={id}')
    def delete_user(self, id):
        return self.delete(url=self.endpoints.delete_user(id))
