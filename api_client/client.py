import requests


def get_user_data(user_id: int) -> str:
    response = requests.get(f'https://api.telegram.org/bot{user_id}').json()
    return f"Hello, {response['name']}"
