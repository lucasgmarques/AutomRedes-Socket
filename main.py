import socket

def verificar_porta(host, porta, portas_abertas, portas_fechadas):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, porta))
        s.close()
        portas_abertas.append(porta)
        print(f"A porta {porta} está aberta")
    except (socket.timeout, ConnectionRefusedError):
        portas_fechadas.append(porta)
        print(f"A porta {porta} está fechada")

def principal():
    host = input("Digite o endereço IP do host: ")
    porta_inicial = int(input("Digite o número da porta inicial: "))
    porta_final = int(input("Digite o número da porta final: "))
    portas_abertas = []
    portas_fechadas = []

    for porta in range(porta_inicial, porta_final + 1):
        verificar_porta(host, porta, portas_abertas, portas_fechadas)

    with open("resultado.log", "w", encoding='utf-8') as output:
        print("Portas abertas:", end=" ", file=output)
        for porta in portas_abertas:
            print(porta, end=", ", file=output)
        print("\nPortas fechadas:", end=" ", file=output)
        for porta in portas_fechadas:
            print(porta, end=", ", file=output)
        print("", file=output)
        print(f"Número de portas abertas: {len(portas_abertas)}", file=output)
        print(f"Número de portas fechadas: {len(portas_fechadas)}", file=output)

if __name__ == "__main__":
    principal()
