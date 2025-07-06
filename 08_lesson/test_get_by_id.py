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


def test_get_by_id():
    resp = requests.post(
        f"{base_url}/api-v2/projects",
        headers=headers,
        json=body)

    new_id = resp.json().get('id')

    requests.get(
        f"{base_url}/api-v2/projects/f{new_id}",
        headers=headers,
        json=body)
    # Проверяем успешный статус создания
    assert resp.status_code == 201
    # Проверяем корректность созданных данных
    response_data = resp.json()
    assert 'id' in response_data


def test_get_by_id_negative():
    requests.post(f"{base_url}/api-v2/projects",
                  headers=headers, json=body)

    new_id = '40'

    resp = requests.get(
        f"{base_url}/api-v2/projects/f{new_id}",
        headers=headers, json=body)
    # Проверяем статус ошибки (не верный ID):
    assert resp.status_code == 404
