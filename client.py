#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

SERVERHOST = 'localhost'
SERVERPORT = 9472

def create_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    return client_socket

def send_message(client_socket):
    msg= input("Digite aqui a sua mensagem: ")

    while msg.lower() != 'tchau':
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()

        print(f"[Servidor]: {data}")

        msg = input(" --> ")

def main():

    client_socket = create_socket(SERVERHOST, SERVERPORT)
    send_message(client_socket)

    print("Finalizando a conexão!")
    client_socket.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("você interrompeu o programa.")
