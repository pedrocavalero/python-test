import unittest
from app import app
from dicionario import dict_to_string

class TestGetDicionario(unittest.TestCase):
    def test_get_dicionario(self):
        with app.test_client() as client:
            response = client.get('/dicionario')
            data = response.get_json()
            expected_result = "nome: Joao, idade: 30, cidade: Sao Paulo"
            self.assertEqual(data, expected_result)

if __name__ == '__main__':
    unittest.main()
