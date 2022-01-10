"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

# ARGS = ['ping', 'youtube.com']
# PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
# for line in PING.stdout:
#     result = chardet.detect(line)
#     print(result['encoding'])
#     line = line.decode(result['encoding']).encode('utf-8')
#     print(line.decode('utf-8'))

URL = ['youtube.com', 'yandex.ru']
PING = 'ping'

for i in range(len(URL)):
    process = subprocess.Popen([PING, URL[i]], stdout=subprocess.PIPE)
    for line in process.stdout:
        coding = chardet.detect(line)
        line = line.decode(coding['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
