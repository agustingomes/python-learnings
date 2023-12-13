import requests
import unittest
from unittest.mock import patch, Mock

def get_user_data(user_id: int) -> dict:
    response = requests.get(f'https://api.telegram.org/bot{user_id}')
    return response.json()

class TestUserData(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data(self, mock_get: Mock):
        mock_response = Mock()
        response_dict = {
            'name': 'Agustin',
            'email': 'agustin@test.com',
        }
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response

        user_data = get_user_data(1)
        mock_get.assert_called_once_with('https://api.telegram.org/bot1')
        self.assertEqual(response_dict, user_data)

if __name__ == '__main__':
    unittest.main()
