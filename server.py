#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import network

def receive_msg(conn, addr):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[Cliente] {addr}: {data.decode()}")
            data = input(' -> ')
            conn.send(data.encode())
    except BrokenPipeError:
        print(f"A conexão com o cliente {addr} foi interrompida.")
    except KeyboardInterrupt:
        print("\nVocê interrompeu o programa.")
    finally:
        conn.close()
        print(f"Conexão finalizada com {addr}.")

def main():
    connections = 0
    host, port = network.set_host_port()
    server_socket = network.create_socket_server(host, port)
    
    try:
        while True:
            print("Aguardando conexão...")
            conn, addr = network.accept_connection(server_socket)
            connections += 1
            receive_msg(conn, addr)
    except KeyboardInterrupt:
        print("Você interrompeu o programa.")
    finally:
        network.close_connection(server_socket)
        print(f"Número de conexões atendidas: {connections}")

if __name__ == "__main__":
    main()
