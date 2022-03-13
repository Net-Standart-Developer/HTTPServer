import socket
import os
import sys
import http

resources = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

def main():
    listen_address = ("", 8080)
    max_connections = 10

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(listen_address)
        server.listen(max_connections)

        while True:
            conn, addr = server.accept()

            with conn:
                manager = http.HTTPManager()
                manager.Handle(conn, addr)

if __name__ == "__main__":
    main()