import requests

base_url = "https://ru.yougile.com/"
api_key = "BcnwwPzIDQxd7jeHEX5nToOFWBJyKh-WNr8yrdWmqg3HvhQcPa3A47EQL64jVZBG"

headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
body = {
    'title': "Новый проект - Руслан"
}

body_negative = {
    'name': "Новый проект - Руслан"
}


def test_create_project():
    resp = requests.post(
        f"{base_url}/api-v2/projects",
        headers=headers,
        json=body)
    # Проверяем успешный статус создания
    assert resp.status_code == 201

    # Проверяем корректность созданных данных
    response_data = resp.json()
    assert 'id' in response_data


def test_create_project_negative():
    resp = requests.post(
        f"{base_url}/api-v2/projects",
        headers=headers,
        json=body_negative)
    # Проверяем статус ошибки создания проекта (не верное тело запроса)
    assert resp.status_code == 400
