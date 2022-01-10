"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

STR_LIST = ['разработка', 'администрирование', 'protocol', 'standard']
ENCODE_LIST = []
DECODE_LIST = []

string = 'encode'
string_encode = string.encode('utf-8')
string_decode = string_encode.decode('utf-8')
print(string)
print(string_encode)
print(string_decode)

def task_funk_encode(lst):
    for word in lst:
        ENCODE_LIST.append(word.encode('utf-8'))
    print(ENCODE_LIST)


def task_funk_decode(lst):
    for word in lst:
        DECODE_LIST.append(word.decode('utf-8'))
    print(DECODE_LIST)

print(STR_LIST)
task_funk_encode(STR_LIST)
task_funk_decode(ENCODE_LIST)
