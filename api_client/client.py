import requests

def get_user_data(user_id: int) -> dict:
    response = requests.get(f'https://api.telegram.org/bot{user_id}')
    return response.json()