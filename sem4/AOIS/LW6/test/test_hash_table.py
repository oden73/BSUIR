import unittest
from hash.hash_table import HashTable



class TestHashTable(unittest.TestCase):
    def test_add_element(self):
        self.hash_table = HashTable()
        self.hash_table.add_element('первый', 'первый')
        self.hash_table.add_element('втор', 'второй')
        self.hash_table.add_element('второй', 'третий')
        self.assertEqual(self.hash_table.get_print_view(), [('втор', '85', '0', '1', '0.0', 'второй'),
                                                            ('второй', '85', '0', '1', '0.1', 'третий'),
                                                            ('первый', '533', '3', '1', '3.0', 'первый')])

    def test_find_element(self):
        self.hash_table = HashTable()
        self.hash_table.add_element('элемент', 'ааааа')
        self.hash_table.add_element('электроник', 'элемент')
        self.assertEqual(self.hash_table.find_by_id('электроник'), 'элемент')

    def test_delete_element(self):
        self.hash_table = HashTable()
        self.hash_table.add_element('первый', 'первый')
        self.hash_table.add_element('втор', 'второй')
        self.hash_table.add_element('второй', 'третий')
        self.hash_table.delete_by_id('второй')
        self.assertEqual(len(self.hash_table.get_print_view()), 2)

    def test_update_element(self):
        self.hash_table = HashTable()
        self.hash_table.add_element('элемент', 'аарраа')
        self.hash_table.update_by_id('элемент', 'замена')
        self.assertEqual(self.hash_table.hash_table[0].Pi, 'замена')
