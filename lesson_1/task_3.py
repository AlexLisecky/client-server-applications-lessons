"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

STR_LIST = ['attribute', 'класс', 'функция', 'type']

def task_funk(lst):
    for word in lst:
        try:
            print(eval(f'b"{word}"'))
        except SyntaxError:
            print(f'невозможно записать в байтовом типе с помощью маркировки: {word}')

task_funk(STR_LIST)