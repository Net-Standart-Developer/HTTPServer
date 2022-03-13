from .Request import Request
from .TypeOfRequest import TypeOfRequest
from main import resources
from . import controllers
import os

class HTTPManager:
    buffer = 4096
    

    def Handle(self, client, addr):
        data = client.recv(HTTPManager.buffer).decode()
        request = Request(data=data)
        
        match request.type:
            case TypeOfRequest.GET:
                controller = controllers.GetController(client, addr)
            case _:
                raise Exception("Неподдерживаемый метод")
        
        controller.HandleRequest(request)
        