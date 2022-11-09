import unittest
from main import people, shelf, add, delete, del_in_shelf, move, add_shelf

class TestFunctionts(unittest.TestCase):
    def SetUp(self) -> None:
        print('метод срабатывает перед тестом')

    def TearDown(self) -> None:
        print('метод срабатывает после теста')

    def test_people(self):
        self.assertEqual(people('11-2'), 'Геннадий Покемонов')

    def test_shelf(self):
        self.assertEqual(shelf('11-2'), 'Документ находится на 1 полке')

    def test_add(self):
        self.assertEqual(add('test', '12345', 'test test', '1'), 'Добавлен в словарь и на полку')

    def test_delete(self):
        self.assertEqual(delete('10006'), 'Документ 10006 удален из списка!')

    def test_del_in_shelf(self):
        self.assertEqual(del_in_shelf('10006'), 'Документ 10006 удален c полки!')

    def test_move(self):
        self.assertEqual(move('2207 876234', '3'), 'Документ 2207 876234 перемещен на 3 полку')

    def test_add_shelf(self):
        self.assertEqual(add_shelf('4'), 'Полка номер 4 создана!')