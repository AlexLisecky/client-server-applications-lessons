import json

from common.settings import ENCODING, MAX_PACKAGE_LENGTH


def send_json_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)


def send_message(sock, message):
    encoded_message = message.encode(ENCODING)
    sock.send(encoded_message)


def get_json_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def get_message(client):
    encoded_responce = client.recv(MAX_PACKAGE_LENGTH)
    responce = encoded_responce.decode(ENCODING)
    return responce
