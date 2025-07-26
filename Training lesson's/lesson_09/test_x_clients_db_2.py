import allure
import pytest
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

@allure.epic("компании")
@allure.severity("blocker")
class CompanyTest:
    api = CompanyApi("http://5.101.50.27:8000")
    db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

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