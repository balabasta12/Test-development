import unittest
from ad import create_folder, delete_folder

class TestYaApi(unittest.TestCase):

    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_create_folder(self):  # Проверка на создание папки
        self.assertEqual(create_folder('test'), 201)

    def test_passed_create_folder(self): # Проверка на сущ. папку
        self.assertEqual(create_folder('test_passed'), 409)

    def test_tearDown(self):  # Удаление папки
        delete_folder('test')
        print('method tearDown')

