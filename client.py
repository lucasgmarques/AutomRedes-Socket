#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import network

def send_message(client_socket):
    try:
        msg= input("Digite aqui a sua mensagem (ou 'f' para fim) :")

        while msg.strip().lower() != 'f':
            client_socket.send(msg.encode())
            data = client_socket.recv(1024).decode()

            print(f"[Servidor] diz: {data}")

            msg = input(" --> ")
    except Exception as e:
        print(f"Erro durante a comunicação: {e}")
    finally:
        print("Finalizando a conexão.")
        client_socket.close()

def main():
    host, port = network.set_host_port()
    client_socket = network.create_socket_client(host, port)
    
    try:
        send_message(client_socket)
    except KeyboardInterrupt:
        print("você interrompeu o programa.")
    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
