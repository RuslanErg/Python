from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from datetime import datetime

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

    assert "id" in result
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1
    for company in body:
        if "id" in company and company["id"] == new_id:
            assert company["name"] == name
            assert company["description"] == descr
            assert company["id"] == new_id


def test_get_one_company():
    #Подготовка
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    #Получение компании
    new_company = api.get_company(max_id)

    #Удаление
    db.delete(max_id)

    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["isActive"] is True

def test_delete():
    #Добавили компанию через базу:
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    #Удалили компанию:
    deleted = api.delete(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

    # Проверили по ID, что компании нет в базе:
    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0

def test_deactivate():
    # Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию
    body = api.set_active_state(new_id, False)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False

def test_deactivate_and_activate_back():
    #Создаем компанию:
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]

    # Деактивируем компанию с помощью параметра False
    body_d = api.set_active_state(new_id, False)

    # Проверяем, что компания не активная
    assert body_d["is_active"] is False

    # Активируем компанию с помощью параметра True
    body_a = api.set_active_state(new_id, True)

    # Проверяем, что компания активная
    assert body_a["is_active"] is True

def test_edit():
    # Добавляем в базу компанию с названием Skypro:
    name = "Skypro"
    db.create(name)
    max_id = db.get_max_id()

    # Меняем описание компании в поле description:
    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit_company(max_id, new_name, new_descr)

    # Удаляем компанию:
    db.delete(max_id)

    assert edited["name"] == new_name
    assert edited["description"] == new_descr