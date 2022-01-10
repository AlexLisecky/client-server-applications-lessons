import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from task_1 import clone_func


class Testclass(unittest.TestCase):

    """"Тест проверки деления : Входные данные 4 , 2 , ожидаем 2"""
    def test_int(self):
        self.assertEqual(clone_func(), 2)

    """"Тест проверки деления : Входные данные 4 , 0 , ожидаем обработку деления на ноль"""
    def test_division_by_zero(self):
        self.assertEqual(clone_func(), "На ноль делить нельзя")

    """"Тест проверки деления : Входные данные "бум" , "крен" , ожидаем валидацию входных данных"""

    def test_string(self):
        self.assertEqual(clone_func(), "Введите число")


if __name__ == '__main__':
    unittest.main()

