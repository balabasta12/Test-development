from main import get_doc_owner_name, add_new_doc, delete_doc
import unittest



class TestFunctions(unittest.TestCase):  #Наследование от базового TestCase
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_show_all_docs_info(self):
        self.assertEqual(get_doc_owner_name('10006'), 'Аристарх Павлов')  # assertEqual == (то, что получим из функции, сравнить)

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('232333', 'pass', 'Iron', 3), 3)

    def test_delete_doc(self):
        self.assertTrue(delete_doc('11-2'))  # assertTrue == (True если бул. знач.)

if __name__ == '__main__':
    unittest.main()