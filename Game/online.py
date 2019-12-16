import socket
import time


def server_init(port):
    # Инициализация сервера
    # Возвращает массив из переменных conn, addr, host.
    # conn - сокет соединения клиента. addr - адрес для соединения. host - имя компа в локальной сети
    # !!! После того, как вы вызвали эту функцию и создали сервер нужно в основной программе
    # создать переменные conn, addr, host, вытянув их из массива, полученного из serverinit
    sock = socket.socket()
    socket.setdefaulttimeout(None)
    host = socket.gethostname()
    sock.bind((host, port))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn, addr, host


def server_send(conn, value):
    # отправляет list (!!!) клиенту
    value_alt = ''
    for i in range(len(value)):
        value_alt += str(value[i]) + '{}'
    print(value_alt)
    conn.send(bytes((str(value_alt)), 'utf-8'))
    return 'sent'


def server_listen(conn):
    # принимает list (!!!)
    stats = []
    stats_alt = ''
    a = conn.recv(1024)
    stats_alt = a.decode(encoding='UTF-8', errors='strict')
    stats = stats_alt.split('{}')
    stats.pop()
    return stats
    return stats


def server_wincheck(conn):
    # проверяет наличие победы у клиента.
    # возвращает "game_over_lost", если другая машина уже выиграла
    # возвращает "game_is_running", если другая машина ещё играет
    conn.settimeout(0.01)
    try:
        data = conn.recv(1024)
        if data == 'tri':
            data = conn.recv(1024)
            data = conn.recv(1024)
            server_send(conn, 'proigral')
        elif data == 'dva':
            data = conn.recv(1024)
            server_send(conn, 'proigral')
        elif data == 'odin':
            server_send(conn, 'proigral')
            conn.close()
            return "game_over_lost"
    except socket.timeout:
        return 'game_is_running'
        pass


def server_iwon(conn):
    # начинает спам о том, что выиграл (осторожно, займёт до секунды времени)
    # возвращает "game_over_won", если вторая машина оповещена
    heard = 0
    while heard == 0:
        conn.send(bytes('tri', 'utf-8'))
        print('iwon')
        conn.send(bytes('dva', 'utf-8'))
        conn.send(bytes('odin', 'utf-8'))
        try:
            conn.settimeout(0.02)
            data = conn.recv(1024)
            if data.decode(encoding='UTF-8', errors='strict') == 'proigral':
                heard = 1
            else:
                pass
        except socket.timeout:
            pass
    conn.close()
    return 'game_over_won'


def client_init(host, port=8888):
    # Инициализация сервера
    # Возвращает массив из переменных conn, addr, host.
    # conn - сокет соединения клиента. addr - адрес для соединения. host - имя компа в локальной сети
    # !!! После того, как вы вызвали эту функцию и создали сервер нужно в основной программе
    # создать переменные conn, addr, host, вытянув их из массива, полученного из serverinit
    sock = socket.socket()
    socket.setdefaulttimeout(None)
    sock.connect((host, port))
    return sock, host


def client_send(sock, value):
    # отправляет list клиенту
    value_alt = ''
    for i in range(len(value)):
        value_alt += str(value[i]) + '{}'
    print(value_alt)
    sock.send(bytes((str(value_alt)), 'utf-8'))
    # conn.send(bytes('stop_t', 'utf-8'))
    return 'sent'


def client_listen(sock):
    stats = []
    stats_alt = ''
    a = sock.recv(1024)
    stats_alt = a.decode(encoding='UTF-8', errors='strict')
    stats = stats_alt.split('{}')
    stats.pop()
    return stats


def client_wincheck(sock):
    sock.settimeout(0.01)
    try:
        data = sock.recv(1024)
        if data == 'tri':
            data = sock.recv(1024)
            data = sock.recv(1024)
            server_send(sock, 'proigral')
        elif data == 'dva':
            data = sock.recv(1024)
            server_send(sock, 'proigral')
        elif data == 'odin':
            server_send(sock, 'proigral')
            sock.close()
            return "game_over_lost"
    except socket.timeout:
        return 'game_is_running'
        pass


def client_iwon(sock):
    heard = 0
    while heard == 0:
        sock.send(bytes('tri', 'utf-8'))
        print('iwon')
        sock.send(bytes('dva', 'utf-8'))
        sock.send(bytes('odin', 'utf-8'))
        try:
            sock.settimeout(0.02)
            data = sock.recv(1024)
            if data.decode(encoding='UTF-8', errors='strict') == 'proigral':
                heard = 1
            else:
                pass
        except socket.timeout:
            pass
    sock.close()
    return 'game_over_won'