from uuid import UUID

import requests

from src.dto import Person, PersonDictionary


def get_user_data(user_id: UUID) -> Person:
    response: PersonDictionary = requests.get(
        f"https://api.telegram.org/bot/{user_id}"
    ).json()
    return Person.from_dict(response)
