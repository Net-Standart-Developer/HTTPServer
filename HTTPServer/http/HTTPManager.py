from threading import Thread
from .Request import Request
from .TypeOfRequest import TypeOfRequest
from main import resources
from . import controllers
import os
import asyncio

class HTTPManager:
    buffer = 4096
    

    async def Handle(self, reader, writer):
        data = (await reader.read(HTTPManager.buffer)).decode()
        request = Request(data=data)

        addr = writer.get_extra_info('peername')
        
        match request.type:
            case TypeOfRequest.GET:
                controller = controllers.GetController(reader, writer, addr)
            case _:
                raise Exception("Неподдерживаемый метод")
        
        await controller.HandleRequest(request)

        writer.close()