import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from task_2 import my_func, my_list


class Testclass(unittest.TestCase):

    """"Тест проверки работы программы : Входные данные [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55] ,
     ожидаем [300,12, 44, 4, 10, 78, 123]
     """
    def test_int(self):
        self.assertEqual(my_func([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]), [300, 12, 44, 4, 10, 78, 123])


if __name__ == '__main__':
    unittest.main()