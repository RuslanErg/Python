from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


def test_get_companies():
    #Шаг1: получить список компаний через API:
    api_result = api.get_company_list()

    #Шаг2: получить список компаний из БД:
    db_result = db.get_companies()

    #Шаг2: проверить, что списки равны
    assert len(api_result) == len(db_result)


def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()

    assert len(filtered_list) == len(db_list)


def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "DescrRRR"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)


    assert len_after - len_before == 1
    for company in body:
            if company["id"] == new_id:
                assert company["name"] == name
                assert company["description"] == descr
                assert company["id"] == new_id


def test_get_one_company():
    #Подготовка
    name = "Skyproooo"
    db.create(name)
    max_id = db.get_max_id()

    #Получение компании
    new_company = api.get_company(max_id)
    print(new_company)
    #Удаление
    db.delete(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["is_active"] is True

