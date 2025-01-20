import socket
import threading
import random

from rsa import decrypt_rsa, encrypt_rsa, load_keys, generate_rsa_keys, save_keys


def receive():
    while True:
        try:
            message = decrypt_rsa(sock.recv(1024), private_key)
            print(f"{message}")
        except Exception as e:
            print(f"Ошибка получения сообщения: {e}")
            break

def send(message):
    sock.send(encrypt_rsa(message, public_key))

def start():
    host = '127.0.0.1'
    port = 5050

    global sock, private_key, public_key
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # RSA
    private_key, public_key = load_keys("client_private.pem", "client_public.pem")
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    while True:
        message = input("Введите сообщение: ")
        if message == "quit":
            break
        send(message)
    sock.close()


if __name__ == "__main__":
    # генерация ключей для клиента
    private_key, public_key = generate_rsa_keys()
    save_keys(private_key, public_key, "client_private.pem", "client_public.pem")
    start()