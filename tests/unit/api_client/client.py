import unittest
import uuid
from unittest.mock import Mock, patch

import src.api_client.client as client


class TestUserData(unittest.TestCase):
    @patch("uuid.uuid4")
    @patch("requests.get")
    def test_get_user_data(
        self,
        mock_get: Mock,
        mock_uuid4: Mock,
    ) -> None:
        uuid_string = "2331c2d9-260a-4f5f-9893-df996fa73782"
        test_uuid = uuid.UUID(uuid_string)
        mock_uuid4.return_value = test_uuid
        mock_get.return_value = Mock(
            json=lambda: {
                "id": uuid_string,
                "name": "Agustin",
                "email": "agustin@test.com",
            }
        )

        # Execute the test
        result_person = client.get_user_data(test_uuid)

        # Assertions
        mock_get.assert_called_once_with(f"https://api.telegram.org/bot/{uuid_string}")
        self.assertEqual(f"Agustin: {uuid_string}", str(result_person))
        self.assertEqual("Agustin", result_person.name)
        self.assertEqual("agustin@test.com", result_person.email)
        self.assertEqual(uuid.UUID(uuid_string), result_person.identity)
        ...
