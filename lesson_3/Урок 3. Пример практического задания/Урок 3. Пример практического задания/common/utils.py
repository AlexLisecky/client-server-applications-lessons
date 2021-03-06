"""Утилиты"""

import json
from common.variables import MAX_PACKAGE_LENGTH, ENCODING

def get_message(client):
    '''
    Утилита приёма и декодирования сообщения
    принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
    :param client:
    :return:
    '''

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    '''
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    '''
    print(message)
    print(type(message))
    js_message = json.dumps(message)
    print(js_message)
    print(type(js_message))
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
