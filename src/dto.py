from dataclasses import dataclass
from typing import TypedDict
from uuid import UUID


@dataclass(frozen=True)
class PersonDictionary(TypedDict):
    id: str
    name: str
    email: str


@dataclass(frozen=True)
class Person:
    identity: UUID
    name: str
    email: str

    def __repr__(self) -> str:
        return f"{self.name}: {str(self.identity)}"

    @staticmethod
    def from_dict(response: PersonDictionary) -> "Person":
        return Person(
            identity=UUID(response["id"]),
            name=response["name"],
            email=response["email"],
        )
