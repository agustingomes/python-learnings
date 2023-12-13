import api_client.client as client
import unittest
from unittest.mock import patch, Mock


class TestUserData(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data(self, mock_get: Mock):
        # Arrange
        mock_response = Mock()
        response_dict = {
            'name': 'Agustin',
            'email': 'agustin@test.com',
        }
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response

        # Act
        user_data = client.get_user_data(1)

        # Assert
        mock_get.assert_called_once_with('https://api.telegram.org/bot1')
        self.assertEqual('Hello, Agustin', user_data)
