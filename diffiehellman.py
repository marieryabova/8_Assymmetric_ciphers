import random
import math

def diffie_hellman(p, g):
    """Реализация протокола Диффи-Хеллмана."""
    # p - большое простое число
    # g - первообразный корень по модулю p

    # Клиентская часть
    a = random.randint(1, p - 2)  # секретный ключ клиента
    A = pow(g, a, p)  # открытый ключ клиента

    # Серверная часть
    b = random.randint(1, p - 2)  # секретный ключ сервера
    B = pow(g, b, p)  # открытый ключ сервера

    # Обмен ключами
    # Клиент получает B от сервера
    # Сервер получает A от клиента

    # Вычисление общего секретного ключа
    shared_secret_client = pow(B, a, p)
    shared_secret_server = pow(A, b, p)

    if shared_secret_client == shared_secret_server:
        return shared_secret_client  # Общий секретный ключ
    else:
        return None
