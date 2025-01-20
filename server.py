import socket
import threading
import random

from rsa import load_keys, decrypt_rsa, encrypt_rsa, generate_rsa_keys, save_keys


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    try:
        # RSA
        private_key, public_key = load_keys("server_private.pem", "server_public.pem")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            ciphertext = data
            plaintext = decrypt_rsa(ciphertext, private_key)
            print(f"Получено от {addr}: {plaintext}")

            message = input(f"Отправить {addr}: ")
            if message == "quit":
                break
            encrypted_message = encrypt_rsa(message, public_key) #шифруем сообщение открытым ключом клиента
            conn.send(encrypted_message)

    except Exception as e:
        print(f"Ошибка обработки клиента {addr}: {e}")
    finally:
        conn.close()
        print(f"[CONNECTION CLOSED] {addr} disconnected.")

def start():
    host = '127.0.0.1'
    port = 5050
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[LISTENING] Server is listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    # генерация ключей для сервера
    private_key, public_key = generate_rsa_keys()
    save_keys(private_key, public_key, "server_private.pem", "server_public.pem")
    start()
