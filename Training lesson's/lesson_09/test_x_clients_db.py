import allure
import pytest
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

@allure.epic("компании")
@allure.severity("blocker")
class CompanyTest:
    api = CompanyApi("http://5.101.50.27:8000")
    db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

    @pytest.fixture(autouse=True)  # Добавляем фикстуру для очистки
    def cleanup(self):
        yield
        self.db.cleanup_test_data()  # Очистка после каждого теста

    @allure.id("SKYPRO-1")
    @allure.story("Получение компаний")
    @allure.feature("READ")
    @allure.epic("компании")
    def test_get_companies(self):
        with allure.step("Получить список компаний через API"):
            api_result = self.api.get_company_list()
        with allure.step("Получить список компаний из БД"):
            db_result = self.db.get_companies()
        with allure.step("Сравнить размеры 2х списков"):
            assert len(api_result) == len(db_result)

    @allure.id("SKYPRO-2")
    @allure.story("Получение списка компаний")
    @allure.feature("READ")
    @allure.title("Получение списка активных организаций")
    @allure.description("Запрос организация с параметром active = true")
    def test_get_active_companies(self):
        filtered_list = self.api.get_company_list(params_to_add={"active": "true"})
        db_list = self.db.get_active_companies()

        assert len(filtered_list) == len(db_list)

    @allure.id("SKYPRO-3")
    @allure.story("Создание компаний")
    @allure.feature("CREATE")
    @allure.title("Создание организации")
    def test_add_new(self):
        with allure.step("Получить количество организаций ДО"):
            body = self.api.get_company_list()
            len_before = len(body)

            with allure.step("Создать организацию"):
                with allure.step("Сгенерировать название"):
                    name = "Autotest"
                    descr = "Descr"

                with allure.step("Вызвать API-метод для создания"):
                    result = self.api.create_company(name, descr)
                    new_id = result["id"]

        with allure.step("Проверить поля новой организации. Корректно заполнены"):
            for company in body:
                if company["id"] == new_id:
                    assert company["name"] == name
                    assert company["description"] == descr
                    assert company["id"] == new_id

        with allure.step("Получить количество организаций после"):
            body = self.api.get_company_list()
            len_after = len(body)

        with allure.step("Проверить, что список ДО меньше списка ПОСЛЕ на 1"):
            assert len_after - len_before == 1

        with allure.step("Удалить из БД новую организацию"):
            self.db.delete(new_id)

    @allure.id("SKYPRO-4")
    @allure.story("Получение компании по id")
    @allure.feature("UPDATE")
    @allure.title("Получение организации по id")
    def test_get_one_company(self):
        #Подготовка
        name = "Skypro"
        self.db.create(name)
        max_id = self.db.get_max_id()

        #Получение компании
        new_company = self.api.get_company(max_id)

        #Удаление
        self.db.delete(max_id)

        assert new_company["id"] == max_id
        assert new_company["name"] == name
        assert new_company["isActive"] is True

    def test_delete(self):
        #Добавили компанию через базу:
        name = "Skypro"
        self.db.create(name)
        max_id = self.db.get_max_id()

        #Удалили компанию:
        deleted = self.api.delete(max_id)

        assert deleted["company_id"] == max_id
        assert deleted["detail"] == "Компания успешно удалена"

        # Проверили по ID, что компании нет в базе:
        rows = self.db.get_company_by_id(max_id)
        assert len(rows) == 0

    def test_deactivate(self):
        # Создаем компанию
        name = "Company to be deactivated"
        result = self.api.create_company(name)
        new_id = result["id"]
        # Деактивируем компанию
        body = self.api.set_active_state(new_id, False)

        # Проверяем, что у компании статус «неактивная»
        assert body["is_active"] is False

    def test_deactivate_and_activate_back(self):
        #Создаем компанию:
        name = "Company to be deactivated"
        result = self.api.create_company(name)
        new_id = result["id"]

        # Деактивируем компанию с помощью параметра False
        body_d = self.api.set_active_state(new_id, False)

        # Проверяем, что компания не активная
        assert body_d["is_active"] is False

        # Активируем компанию с помощью параметра True
        body_a = self.api.set_active_state(new_id, True)

        # Проверяем, что компания активная
        assert body_a["is_active"] is True

    def test_edit(self):
        # Добавляем в базу компанию с названием Skypro:
        name = "Skypro"
        self.db.create(name)
        max_id = self.db.get_max_id()

        # Меняем описание компании в поле description:
        new_name = "Updated"
        new_descr = "_upd_"
        edited = self.api.edit_company(max_id, new_name, new_descr)

        # Удаляем компанию:
        self.db.delete(max_id)

        assert edited["name"] == new_name
        assert edited["description"] == new_descr