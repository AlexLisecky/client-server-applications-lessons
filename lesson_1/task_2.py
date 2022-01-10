"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

STR_LIST = [b'class', b'function', b'method']
string = 'apple'
print(eval(f'b"{string}"'))
print(string)
x = 1
print(eval('x + 1'))

def task_funk(lst):
    for word in lst:
        print(type(word))
        print(word)
        print(len(word))


task_funk(STR_LIST)
