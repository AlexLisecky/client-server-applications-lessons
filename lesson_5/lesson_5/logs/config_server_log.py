"""Кофнфиг серверного логгера"""

import sys
import os
import logging
import logging.handlers
from common.variables import LOGGING_LEVEL,MAX_CONNECTIONS
sys.path.append('../')

# создаём формировщик логов (formatter):
SERVER_FORMATTER = logging.Formatter('%(asctime)s ----- %(levelname)-10s %(filename)s ----- %(message)s')
TEST_SERVER_FORMATTER = logging.Formatter('%(asctime)s ----- %(levelname)-10s %(filename)s ----- %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')
TEST_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_PATH = os.path.join(TEST_PATH, 'test_server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)
TEST_LOG_FILE = logging.FileHandler(TEST_PATH, encoding='utf-8')
TEST_LOG_FILE.setFormatter(TEST_SERVER_FORMATTER)

# создаём регистратор и настраиваем его
TEST_LOGGER = logging.getLogger('test_server')
TEST_LOGGER.addHandler(TEST_LOG_FILE)
TEST_LOGGER.addHandler(TEST_LOG_FILE)
TEST_LOGGER.setLevel(logging.DEBUG)
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
    TEST_LOGGER.debug('Тестовый запуск')
