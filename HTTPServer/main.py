import socket
import os
import sys
import http
import asyncio

resources = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

async def main():
    listen_address = ("127.0.0.1", 8080)
    max_connections = 10

    manager = http.HTTPManager()

    server = await asyncio.start_server(
        manager.Handle, listen_address[0], listen_address[1])

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())