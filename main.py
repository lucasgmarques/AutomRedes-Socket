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

def registrar_log(portas_abertas, portas_fechadas):
    with open("log.txt", "w", encoding='utf-8') as arquivo_log:
        arquivo_log.write(f"Portas abertas: {', '.join(map(str, portas_abertas))}\n")
        arquivo_log.write(f"Portas fechadas: {', '.join(map(str, portas_fechadas))}\n")
        arquivo_log.write(f"Número de portas abertas: {len(portas_abertas)}\n")
        arquivo_log.write(f"Número de portas fechadas {len(portas_fechadas)}")
        arquivo_log.close()

def principal():
    host = input("Digite o endereço IP do host a ser verificado: ")
    porta_inicial = int(input("Digite o número da porta de início: "))
    porta_final = int(input("Digite o número da porta de término: "))
    
    portas_abertas = []
    portas_fechadas = []

    for porta in range(porta_inicial, porta_final + 1):
        verificar_porta(host, porta, portas_abertas, portas_fechadas)

    print(f"Portas abertas: {', '.join(map(str, portas_abertas))}")
    print(f"Portas fechadas: {', '.join(map(str, portas_fechadas))}")

    registrar_log(portas_abertas, portas_fechadas)
    print("Resultados registrados em 'log.txt'.")

if __name__ == "__main__":
    principal()
