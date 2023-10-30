import socket

def verificar_porta(host, porta):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(3)

        s.connect((host, porta))

        print(f"A porta {porta} está aberta")

        s.close()
    except (socket.timeout, ConnectionRefusedError):
        print(f"A porta {porta} está fechada")

def principal():
    host = socket.gethostbyname(socket.gethostname())
    for porta in range(1, 1025):
        verificar_porta(host, porta)

if __name__ == "__main__":
    principal()
