import requests
import allure

class CompanyApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    @allure.step("api. Получить список компаний через API")
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company/list', params=params_to_add)
        return resp.json()

    @allure.step("api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user='harrypotter', password='expelliarmus'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]

    @allure.step("api. Создать компанию {name} ({description})")
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/company/create',
                             json=company)
        return resp.json()

    @allure.step("api. Получить компанию по {id}")
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    @allure.step("api. Редактировать компанию {new_id}. {new_name} ({new_descr})")
    def edit_company(self, new_id, new_name, new_descr):
        # Получаем токен
        client_token = self.get_token()

        # Формируем URL с параметром client_token
        url_with_token = (f"{self.url}/company/update/{new_id}"
                          f"?client_token={client_token}")

        # Вызываем словарь и кладем в него описание компании
        company = {
            "name": new_name,  # Новое имя компании
            "description": new_descr  # Новое описание компании
        }

        # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.patch(url_with_token, json=company)

        # Результат вернется в JSON, мы его прокинем в тест
        return resp.json()

    @allure.step("api. Удалить компанию {id}")
    def delete_company(self, id):
        client_token = self.get_token()

        # Формируем URL с параметром client_token
        url_with_token = (f"{self.url}/company/{id}?"
                          f"client_token={client_token}")

        # Метод отправляет DELETE-запрос
        resp = requests.delete(url_with_token)

        # Возвращаем JSON-ответ
        return resp.json()

    @allure.step("api. (Де)активировать компанию {id} -> {isActive}")
    def set_active_state(self, id, is_active):
        client_token = self.get_token()

        url_with_token = (f"{self.url}/company/status_update/{id}"
                          f"?client_token={client_token}")
        resp = requests.patch(url_with_token,
                              json={"is_active": is_active})
        return resp.json()