from api.clients.base_api import BaseAPI
import allure


class AuthAPI(BaseAPI):

    @allure.step('Получение токена авторизации')
    def auth_token_api(self):
        response = self.post(url=self.endpoints.auth, json=self.payloads.auth_payload())
        self.attach_response(response.text)
        return response

    @allure.step('Получение токена авторизации где username={username}, password={password}')
    def get_auth_token_api(self, username: str, password: str):
        response = self.post(url=self.endpoints.auth, json={"username": username, "password": password})
        return response
