"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""
from chardet import detect

# Эту часть сделал для примера записи в другой кодировке(у меня по умолчанию записывалось в utf-8)
with open('test_file.txt', 'w', encoding='cp866') as t_f:
    t_f.write('сетевое программирование\n')
    t_f.write('сокет\n')
    t_f.write('декоратор\n')


def encoding():
    with open('test_file.txt', 'rb') as t_f:
        content_bytes = t_f.read()
        print(content_bytes)
    detected = detect(content_bytes)
    print(detected)
    encoding = detected['encoding']
    print(encoding)
    content_text = content_bytes.decode(encoding)
    print(content_text)
    with open('test_file.txt', 'w', encoding='utf-8') as t_f:
        t_f.write(content_text)


encoding()

with open('test_file.txt.', 'r', encoding='utf-8') as t_f:
    content = t_f.read()
print(content)
